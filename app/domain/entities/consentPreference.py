from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ConsentPreference(BaseModel):
    row_id: Optional[int]
    consent_row_id: int  # FK to Consent.row_id
    name: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True