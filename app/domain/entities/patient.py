from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class Patient(BaseModel):
    row_id: int  # FK to Event.row_id
    first_name: str
    last_name: str
    birth_date: date
    gender: Optional[str] = None
    preferred_language_code: Optional[str] = None
    name_prefix_code: Optional[str] = None
    name_suffix_code: Optional[str] = None
    middle_name: Optional[str] = None
    mdm_id: str
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True