from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class ConsentPreferencesOptionSchema(BaseModel):
    selected_option: str