from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import Any
from app.db.models.apiRequestResponse import ApiRequestResponse

def log_db_upload(request_data: dict[str, Any], response_data: dict[str, Any], db: Session):
    apiRequestResponse = ApiRequestResponse(
        request_data=request_data,
        response_data=response_data
    )
    db.add(apiRequestResponse)
    db.flush()

    db.commit()