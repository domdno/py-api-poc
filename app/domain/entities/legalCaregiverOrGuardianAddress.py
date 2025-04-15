from typing import Optional
from pydantic import BaseModel

class LegalCaregiverOrGuardianAddress(BaseModel):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state_or_province_code: Optional[str] = None
    country_code: Optional[str] = None
    postal_code: Optional[str] = None
    enriched_indicator: Optional[str] = None

    class Config:
        from_attributes = True