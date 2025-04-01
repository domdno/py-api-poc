from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class PatientAlternateContactSchema(BaseModel):
    full_name: str
    relationship_to_patient: str
    phone_number: Optional[str] = None
    email_address: Optional[str] = None