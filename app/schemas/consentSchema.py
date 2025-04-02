from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

from app.schemas.consentPreferenceSchema import ConsentPreferenceSchema

class ConsentSchema(BaseModel):
    name: str
    status: str
    preferences: Optional[List[ConsentPreferenceSchema]]