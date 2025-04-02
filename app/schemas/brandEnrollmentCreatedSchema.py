from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from app.schemas.brandEnrollmentDataSchema import BrandEnrollmentDataSchema

class BrandEnrollmentCreatedSchema(BaseModel):
    event_type: str = Field(..., alias="eventType")
    version: str
    created_timestamp: datetime = Field(..., alias="createdTimestamp")
    request_id: Optional[str] = Field(alias="requestId")
    data: BrandEnrollmentDataSchema