from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Event(BaseModel):
    event_type: str
    version: str
    created_timestamp: datetime
    request_id: Optional[str]

    class Config:
        from_attributes = True
