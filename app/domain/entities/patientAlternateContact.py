from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PatientAlternateContact(BaseModel):
    row_id: int  # FK to Event.row_id
    full_name: str
    relationship_to_patient: str
    phone_number: Optional[str] = None
    email_address: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True