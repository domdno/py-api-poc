from app.db.models.patient import Patient as PatientDBModel
from app.domain.entities.patient import Patient as PatientEntity

# Schema -> Entity
def schema_to_patient_entity(payload) -> PatientEntity:
    entity_data = payload.model_dump(by_alias=False)
    return PatientEntity(**entity_data)

# Entity -> DB Model
def patient_entity_to_db_model(entity: PatientEntity, event_row_id: int):
    return PatientDBModel(
        row_id=event_row_id,
        first_name=entity.first_name,
        last_name=entity.last_name,
        birth_date=entity.birth_date,
        gender=entity.gender,
        preferred_language_code=entity.preferred_language_code,
        name_prefix_code=entity.name_prefix_code,
        name_suffix_code=entity.name_suffix_code,
        middle_name=entity.middle_name,
        mdm_id=entity.mdm_id,
        is_active=entity.is_active
    )