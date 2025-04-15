from typing import Optional
from pydantic import BaseModel

class LegalCaregiverOrGuardianCommunication(BaseModel):
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True