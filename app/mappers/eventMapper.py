from app.db.models.event import Event as EventDBModel
from app.domain.entities.event import Event as EventEntity

# Schema -> Entity
def schema_to_event_entity(payload) -> EventEntity:
    return EventEntity(
        event_type=payload.event_type,
        version=payload.version,
        created_timestamp=payload.created_timestamp,
        request_id=payload.request_id
    )

# Entity -> DB Model
def event_entity_to_db_model(entity: EventEntity) -> EventDBModel:
    return EventDBModel(
        event_type=entity.event_type,
        version=entity.version,
        created_timestamp=entity.created_timestamp,
        request_id=entity.request_id
    )