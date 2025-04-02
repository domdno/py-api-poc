from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class PatientCommunication(BaseModel):
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True