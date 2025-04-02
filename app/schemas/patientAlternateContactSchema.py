from typing import Optional
from pydantic import BaseModel, Field

class PatientAlternateContactSchema(BaseModel):
    full_name: str = Field(..., alias="fullName")
    relationship_to_patient: str = Field(..., alias="relationshipToPatient")
    phone_number: Optional[str] = Field(alias="phoneNumber", default=None)
    email_address: Optional[str] = Field(alias="emailAddress", default=None)