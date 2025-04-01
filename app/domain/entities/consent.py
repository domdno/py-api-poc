from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Consent(BaseModel):
    row_id: Optional[int]
    patient_row_id: int  # FK to Event.row_id (or Patient.row_id)
    name: str
    status: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True