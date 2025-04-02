from datetime import datetime
from typing import List
from pydantic import BaseModel, Field

class ConsentPreferenceSchema(BaseModel):
    name: str
    selected_options: List[str] = Field(..., alias="selectedOptions")