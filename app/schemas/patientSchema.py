from datetime import date
from typing import Optional, List
from pydantic import BaseModel, Field

from app.schemas.patientCommunicationSchema import PatientCommunicationSchema
from app.schemas.patientAlternateContactSchema import PatientAlternateContactSchema
from app.schemas.legalCaregiverOrGuardianSchema import LegalCaregiverOrGuardianSchema

class PatientSchema(BaseModel):
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    birth_date: date = Field(..., alias="birthDate")
    gender: Optional[str] = None
    preferred_language_code: Optional[str] = Field(alias="preferredLanguageCode", default=None)
    name_prefix_code: Optional[str] = Field(alias="namePrefixCode", default=None)
    name_suffix_code: Optional[str] = Field(alias="nameSuffixCode", default=None)
    middle_name: Optional[str] = Field(alias="middleName", default=None)
    mdm_id: str = Field(..., alias="id")
    is_active: Optional[bool] = Field(alias="isActive", default=True)
    address_line1: str = Field(..., alias="addressLine1")
    address_line2: Optional[str] = Field(alias="addressLine2", default=None)
    city: str
    state_or_province_code: str = Field(..., alias="stateOrProvinceCode")
    country_code: str = Field(..., alias="countryCode")
    postal_code: str = Field(..., alias="postalCode")
    enriched_indicator: Optional[str] = Field(alias="enrichedIndicator", default=None)
    communications: List[PatientCommunicationSchema]
    alternate_contact: Optional[PatientAlternateContactSchema] = None
    legal_caregiver_or_guardian: Optional[LegalCaregiverOrGuardianSchema] = None

    class Config:
        validate_by_name = True 