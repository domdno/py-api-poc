from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class Event(BaseModel):
    event_type: str
    version: str
    created_timestamp: datetime
    request_id: Optional[str]

    class Config:
        orm_mode = True
