from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from app.db.models.consent import Consent
from app.db.models.consentPreference import ConsentPreference
from app.db.models.consentPreferenceOption import ConsentPreferenceOption
from app.db.models.patient import Patient

async def get_single_latest_consents(mdm_id: str, consent: str, db: AsyncSession):
    """
    Service to get latest consent for a given mdm_id

    Limited to a specific consent name
    """

    # TODO: re-write to limit number of queries (N+1)
    # TODO: add error handling if patient_row_ids is null

    # create CTE to get all patient row_ids for given mdm_id
    patient_row_ids = (
        select(Patient.row_id)
        .where(Patient.mdm_id == mdm_id)
        .cte("patient_row_ids")
    )

    # create CTE to get latest created_at for each consent name
    latest_created_at = (
        select(
            Consent.name,
            func.max(Consent.created_at).label('max_created_at')
        )
        .join(
            patient_row_ids,
            Consent.patient_row_id == patient_row_ids.c.row_id
            )
        .where(Consent.name == consent)
        .group_by(Consent.name)
        .cte("latest_created_at")
    )

    # query to join consent against both CTEs
    latest_consents_query = (
        select(Consent)
        .join(
            latest_created_at,
            (Consent.name == latest_created_at.c.name)
            & (Consent.created_at == latest_created_at.c.max_created_at)
            )
        .join(
            patient_row_ids,
            Consent.patient_row_id == patient_row_ids.c.row_id
        )
    )
    latest_consents = (await db.execute(latest_consents_query)).scalars().all()

    # build final output list
    result = []
    for consent_obj in latest_consents:

        # get preferences for each consent_obj
        consent_preferences_query = (
            select(ConsentPreference)
            .where(
                ConsentPreference.consent_row_id == consent_obj.row_id
            )
        )
        consent_preferences = (await db.execute(consent_preferences_query)).scalars().all()
        

        # build preferences list
        preferences = []
        for preference in consent_preferences:
            
            # get selected options for each preference
            options_query = (
                select(ConsentPreferenceOption.selected_option)
                .where(
                    ConsentPreferenceOption.consent_preference_row_id == preference.row_id
                )
            )
            options = (await db.execute(options_query)).scalars().all()

            # append array of options to each preference
            preferences.append({
                "name": preference.name,
                "selectedOptions": options
            })

        # append array of preferences to each consent
        result.append({
            "name": consent_obj.name,
            "status": consent_obj.status,
            "preferences": preferences
        })

    # return query result
    return result