from sqlalchemy.orm import Session
from app.schemas.brandEnrollmentCreatedSchema import BrandEnrollmentCreatedSchema
from app.db.models.consent import Consent
from app.db.models.consentPreference import ConsentPreference
from app.db.models.consentPreferenceOption import ConsentPreferenceOption
from app.db.models.enrollmentEvent import EnrollmentEvent
from app.db.models.event import Event
from app.db.models.legalCaregiverOrGuardian import LegalCaregiverOrGuardian
from app.db.models.legalCaregiverOrGuardianAddress import LegalCaregiverOrGuardianAddress
from app.db.models.legalCaregiverOrGuardianCommunication import LegalCaregiverOrGuardianCommunication
from app.db.models.patient import Patient
from app.db.models.patientAddress import PatientAddress
from app.db.models.patientAlternateContact import PatientAlternateContact
from app.db.models.patientCommunication import PatientCommunication

def create_enrollment(payload: BrandEnrollmentCreatedSchema, db: Session):
    """
    This is how we map to the db
    First we need to insert the event to get the row_id to be used in the
        other tables
    """
    event = Event(
        event_type=payload.event_type,
        version=payload.version,
        created_timestamp=payload.created_timestamp,
        request_id=payload.request_id
    )
    db.add(event)
    db.flush() # using flush() allows us to use row_id from the table

    # TODO: add enrollment_event mapping

    patient_data = payload.data.patient
    patient = Patient(
        row_id=event.row_id,  # use event.row_id as the FK
        first_name=patient_data.first_name,
        last_name=patient_data.last_name,
        birth_date=patient_data.birth_date,
        gender=patient_data.gender,
        preferred_language_code=patient_data.preferred_language_code,
        name_prefix_code=patient_data.name_prefix_code,
        name_suffix_code=patient_data.name_suffix_code,
        middle_name=patient_data.middle_name,
        mdm_id=patient_data.mdm_id,
        is_active=patient_data.is_active
    )
    db.add(patient)
    db.flush()  # get patient.row_id

    """
    This is how we handle nesting
    We will db.add() for each object in the array
    """
    for comm in patient_data.communications:
        patient_comm = PatientCommunication(
            row_id=patient.row_id,  # FK to Patient
            value=comm.value,
            type=comm.type,
            is_primary=comm.is_primary,
            status=comm.status
        )
        db.add(patient_comm)

    # TODO: add patient address mapping

    """
    This is how we handle optional objects
    If alternate_contact is null, we don't add anything to the db
    """
    if patient_data.alternate_contact:
        alt_contact = PatientAlternateContact(
            row_id=patient.row_id,
            full_name=patient_data.alternate_contact.full_name,
            relationship_to_patient=patient_data.alternate_contact.relationship_to_patient,
            phone_number=patient_data.alternate_contact.phone_number,
            email_address=patient_data.alternate_contact.email_address
        )
        db.add(alt_contact)

    
    if patient_data.legal_caregiver_or_guardian:
        caregiver_data = patient_data.legal_caregiver_or_guardian
        caregiver = LegalCaregiverOrGuardian(
            row_id=patient.row_id,  
            data_provider_caregiver_id=caregiver_data.data_provider_caregiver_id,
            relationship_to_patient=caregiver_data.relationship_to_patient,
            caregiver_mdm_id=caregiver_data.caregiver_mdm_id,
            first_name=caregiver_data.first_name,
            last_name=caregiver_data.last_name,
            birth_date=caregiver_data.birth_date,
            gender=caregiver_data.gender,
            preferred_language_code=caregiver_data.preferred_language_code,
            name_prefix_code=caregiver_data.name_prefix_code,
            name_suffix_code=caregiver_data.name_suffix_code,
            middle_name=caregiver_data.middle_name,
        )
        db.add(caregiver)
        db.flush()

        
        for comm in caregiver_data.communications:
            caregiver_comm = LegalCaregiverOrGuardianCommunication(
                row_id=caregiver.row_id,
                value=comm.value,
                type=comm.type,
                is_primary=comm.is_primary,
                status=comm.status
            )
            db.add(caregiver_comm)

        
        caregiver_address = LegalCaregiverOrGuardianAddress(
            row_id=caregiver.row_id,
            address_line1=caregiver_data.address_line1,
            address_line2=caregiver_data.address_line2,
            city=caregiver_data.city,
            state_or_province_code=caregiver_data.state_or_province_code,
            country_code=caregiver_data.country_code,
            postal_code=caregiver_data.postal_code,
            enriched_indicator=caregiver_data.enriched_indicator
        )
        db.add(caregiver_address)

    
    for consent_data in payload.data.consent:
        consent = Consent(
            patient_row_id=patient.row_id,
            name=consent_data.name,
            status=consent_data.status
        )
        db.add(consent)
        db.flush()  # flush to get consent.row_id

        if consent_data.preferences:
            for pref_data in consent_data.preferences:
                preference = ConsentPreference(
                    consent_row_id=consent.row_id,
                    name=pref_data.name
                )
                db.add(preference)
                db.flush()  # flush to get preference.row_id

                for option in pref_data.selected_options:
                    option_obj = ConsentPreferenceOption(
                        consent_preference_row_id=preference.row_id,
                        selected_option=option
                    )
                    db.add(option_obj)

    # commit only if all inserts are successful
    db.commit()
    
    # Return the same payload as confirmation
    return payload