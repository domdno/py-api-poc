from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class LegalCaregiverOrGuardian(BaseModel):
    row_id: int  # FK to Event.row_id
    data_provider_caregiver_id: str
    relationship_to_patient: Optional[str] = None
    caregiver_mdm_id: Optional[str] = None
    first_name: str
    last_name: str
    birth_date: date
    gender: Optional[str] = None
    preferred_language_code: Optional[str] = None
    name_prefix_code: Optional[str] = None
    name_suffix_code: Optional[str] = None
    middle_name: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True