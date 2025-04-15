from typing import Optional
from pydantic import BaseModel

class PatientAlternateContact(BaseModel):
    full_name: str
    relationship_to_patient: str
    phone_number: Optional[str] = None
    email_address: Optional[str] = None

    class Config:
        orm_mode = True