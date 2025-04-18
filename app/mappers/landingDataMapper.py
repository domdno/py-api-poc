from fastapi.encoders import jsonable_encoder

from app.db.models.landingData import LandingData as LandingDataDBModel
from app.domain.entities.landingData import LandingData as LandingDataEntity

# Schema -> Entity
def schema_to_landing_data_entity(method, path, payload) -> LandingDataEntity:
    return LandingDataEntity(
        request_method=method,
        request_path=path,
        request_data=jsonable_encoder(payload)
    )

# Entity -> DB Model
def landing_data_entity_to_db_model(entity: LandingDataEntity) -> LandingDataDBModel:
    return LandingDataDBModel(
        request_method=entity.request_method,
        request_path=entity.request_path,
        request_data=entity.request_data
    )