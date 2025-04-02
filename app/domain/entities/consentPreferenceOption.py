from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel
from dataclasses import dataclass

@dataclass
class ConsentPreferencesOption(BaseModel):
    selected_option: str

    class Config:
        orm_mode = True