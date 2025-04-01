from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class LegalCaregiverOrGuardianCommunicationSchema(BaseModel):
    value: str
    type: str
    is_primary: Optional[bool] = None
    status: Optional[str] = None