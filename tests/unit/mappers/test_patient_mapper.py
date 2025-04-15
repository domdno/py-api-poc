import datetime
import pytest

from app.schemas.patientSchema import PatientSchema
from app.db.models.patient import Patient as PatientDBModel
from app.domain.entities.patient import Patient as PatientEntity
from app.mappers.patientMapper import schema_to_patient_entity, patient_entity_to_db_model

def create_sample_patient_schema_instance() -> PatientSchema:
    # sample payload JSON
    sample_data = {
        "firstName": "John",
        "lastName": "Smith",
        "birthDate": "1990-01-01",
        "gender": "male",
        "preferredLanguageCode": "en",
        "namePrefixCode": "Mr",
        "nameSuffixCode": "Jr",
        "middleName": "C",
        "id": "MDM1000000000",
        "isActive": True,
        "addressLine1": "123 Main St",
        "addressLine2": "Appt 1",
        "city": "New York",
        "stateOrProvinceCode": "NY",
        "countryCode": "US",
        "postalCode": "10001",
        "enrichedIndicator": "yes",
        "communications": [],
    }
    return PatientSchema(**sample_data)

# test schema_to_patient_entity()
def test_schema_to_patient_entity():
    # create sample PatientSchema/payload
    sample_payload = create_sample_patient_schema_instance()

    # perform mapping
    sample_entity = schema_to_patient_entity(sample_payload)

    # verify mapping
    assert isinstance(sample_entity, PatientEntity)
    assert sample_entity.first_name == sample_payload.first_name
    assert sample_entity.last_name == sample_payload.last_name
    assert sample_entity.birth_date == sample_payload.birth_date
    assert sample_entity.gender == sample_payload.gender
    assert sample_entity.preferred_language_code == sample_payload.preferred_language_code
    assert sample_entity.name_prefix_code == sample_payload.name_prefix_code
    assert sample_entity.name_suffix_code == sample_payload.name_suffix_code
    assert sample_entity.middle_name == sample_payload.middle_name
    assert sample_entity.mdm_id == sample_payload.mdm_id
    assert sample_entity.is_active == sample_payload.is_active

# test patient_entity_to_db_model()
def test_patient_entity_to_db_model():
    # create sample entity
    sample_entity = PatientEntity(
        first_name="John",
        last_name="Smith",
        birth_date=datetime.date(1990, 1, 1),
        gender="male",
        preferred_language_code="en",
        name_prefix_code="Mr",
        name_suffix_code="Jr",
        middle_name="C",
        mdm_id="MDM1000000000",
        is_active=True
    )
    event_row_id = 123

    # perform mapping
    sample_db_model = patient_entity_to_db_model(sample_entity, event_row_id)

    # verify mapping
    assert isinstance(sample_db_model, PatientDBModel)
    assert sample_db_model.row_id == event_row_id
    assert sample_db_model.first_name == sample_entity.first_name
    assert sample_db_model.last_name == sample_entity.last_name
    assert sample_db_model.birth_date == sample_entity.birth_date
    assert sample_db_model.gender == sample_entity.gender
    assert sample_db_model.preferred_language_code == sample_entity.preferred_language_code
    assert sample_db_model.name_prefix_code == sample_entity.name_prefix_code
    assert sample_db_model.name_suffix_code == sample_entity.name_suffix_code
    assert sample_db_model.middle_name == sample_entity.middle_name
    assert sample_db_model.mdm_id == sample_entity.mdm_id
    assert sample_db_model.is_active == sample_entity.is_active