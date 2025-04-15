from typing import Optional
from pydantic import BaseModel

class PatientAddress(BaseModel):
    address_line1: str
    address_line2: Optional[str] = None
    city: str
    state_or_province_code: str
    country_code: str
    postal_code: str
    enriched_indicator: Optional[str] = None

    class Config:
        orm_mode = True