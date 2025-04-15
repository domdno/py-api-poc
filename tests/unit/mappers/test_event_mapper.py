import datetime
import uuid
import pytest

from app.db.models.event import Event as EventDBModel
from app.domain.entities.event import Event as EventEntity
from app.mappers.eventMapper import schema_to_event_entity, event_entity_to_db_model


# sample payload class for testing
class SamplePayload:
    def __init__(self, event_type, version, created_timestamp, request_id):
        self.event_type=event_type
        self.version=version
        self.created_timestamp=created_timestamp
        self.request_id=request_id

# test schema_to_event_entity()
def test_schema_to_event_entity():
    # create sample payload
    sample_payload = SamplePayload(
        event_type="test_event",
        version="1.0",
        created_timestamp=datetime.datetime(2025, 4, 11),
        request_id=str(uuid.uuid4())
    )

    # perform mapping
    sample_entity = schema_to_event_entity(sample_payload)

    # verify mapping
    assert isinstance(sample_entity, EventEntity)
    assert sample_entity.event_type == sample_payload.event_type
    assert sample_entity.version == sample_payload.version
    assert sample_entity.created_timestamp == sample_payload.created_timestamp
    assert sample_entity.request_id == sample_payload.request_id

# test event_entity_to_db_model()
def test_event_entity_to_db_model():
    # create sample entity
    sample_entity = EventEntity(
        event_type="test_event",
        version="1.0",
        created_timestamp=datetime.datetime(2025, 4, 11),
        request_id=str(uuid.uuid4())
    )

    # perform mapping
    sample_db_model = event_entity_to_db_model(sample_entity)

    # verify mapping
    assert isinstance(sample_db_model, EventDBModel)
    assert sample_db_model.event_type == sample_entity.event_type
    assert sample_db_model.version == sample_entity.version
    assert sample_db_model.created_timestamp == sample_entity.created_timestamp
    assert sample_db_model.request_id == sample_entity.request_id