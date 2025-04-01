from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class LegalCaregiverOrGuardianCommunication(BaseModel):
    row_id: int  # FK to LegalCaregiverOrGuardian.row_id
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True