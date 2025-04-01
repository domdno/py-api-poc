from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Consent(BaseModel):
    name: str
    status: str

    class Config:
        orm_mode = True