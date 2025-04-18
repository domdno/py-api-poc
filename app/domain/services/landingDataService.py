import json
from app.db.database import async_get_db
from typing import Any
from app.mappers.landingDataMapper import (
    schema_to_landing_data_entity,
    landing_data_entity_to_db_model
)

from app.repositories.landingDataRepository import save_landing_data

async def landing_data_service(method: str, path: str, payload):
    async for db in async_get_db():
        try:
            landing_data_entity = schema_to_landing_data_entity(
                method,
                path,
                payload
            )
            landing_data_model = landing_data_entity_to_db_model(landing_data_entity)
            await save_landing_data(landing_data_model, db)
            await db.commit()
        except Exception as e:
            print(f"Logging error: {e}")
            raise e
        break