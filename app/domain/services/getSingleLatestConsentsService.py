from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.models.consent import Consent
from app.db.models.consentPreference import ConsentPreference
from app.db.models.consentPreferenceOption import ConsentPreferenceOption
from app.db.models.patient import Patient

def get_single_latest_consents(mdm_id: str, consent: str, db: Session):
    """
    This is how we get the latest consent for a patient

    If consent is passed as a query param, we will limit the query to a
        single consent purpose
    """

    # TODO: add error handling if patient mdm_id is not found
    # use subquery to get all patient row_ids for given mdm_id
    patient_subquery = (
        db.query(Patient.row_id)
        .filter(Patient.mdm_id == mdm_id)
        .subquery()
    )

    # TODO: add error handling if consent name is invalid
    # use subquery to get latest created_at for given consent name
    latest_subquery = (
        db.query(
            Consent.name,
            func.max(Consent.created_at).label('max_created_at')
        )
        .join(
            patient_subquery,
            Consent.patient_row_id == patient_subquery.c.row_id)
        .filter(Consent.name == consent)
        .group_by(Consent.name)
        .subquery()
    )

    # join consent table with latest_subquery
    latest_consents = (
        db.query(Consent)
        .join(latest_subquery,
              (Consent.name == latest_subquery.c.name) &
              (Consent.created_at == latest_subquery.c.max_created_at)
              )
        .join(
            patient_subquery,
            Consent.patient_row_id == patient_subquery.c.row_id)
        .all()
    )

    # build final output list
    result = []
    for consent_obj in latest_consents:

        # get preferences for each consent_obj
        consent_preferences = (
            db.query(ConsentPreference)
            .filter(ConsentPreference.consent_row_id == consent_obj.row_id)
            .all()
        )

        # build preferences list
        preferences = []
        
        # get selected options for each preference
        for preference in consent_preferences:
            options = (
                db.query(ConsentPreferenceOption)
                .filter(ConsentPreferenceOption.consent_preference_row_id == preference.row_id)
                .all()
            )
            selected_options = [option.selected_option for option in options]

            preference_data = {
                "name": preference.name,
                "selectedOptions": selected_options
            }

            # add to preferences list
            preferences.append(preference_data)

        consent_data = {
            "name": consent_obj.name,
            "status": consent_obj.status,
            "preferences": preferences
        }
        result.append(consent_data)

    # return query result
    return result