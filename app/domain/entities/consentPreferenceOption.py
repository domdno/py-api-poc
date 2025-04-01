from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class ConsentPreferencesOption(BaseModel):
    row_id: Optional[int]
    consent_preference_row_id: int  # FK to ConsentPreference.row_id
    selected_option: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True