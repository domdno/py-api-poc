from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class ConsentPreference(BaseModel):
    name: str

    class Config:
        orm_mode = True