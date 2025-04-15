from typing import Optional
from pydantic import BaseModel

class PatientCommunication(BaseModel):
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True