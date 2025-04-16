import json
from app.db.database import async_get_db
from typing import Any
from app.db.models.apiRequestResponse import ApiRequestResponse

async def log_db_upload(request_data: dict[str, Any], response_data: dict[str, Any]):
    async for db in async_get_db():
        try:
            apiRequestResponse = ApiRequestResponse(
                request_data=json.dumps(request_data),
                response_data=json.dumps(response_data)
            )
            db.add(apiRequestResponse)
            await db.commit()
        except Exception as e:
            print(f"Logging error: {e}")
            raise e
        break