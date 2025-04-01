from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ConsentPreferenceSchema(BaseModel):
    name: str