from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PatientCommunication(BaseModel):
    row_id: int  # FK to Event.row_id
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True