from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field

from app.schemas.legalCaregiverOrGuardianCommunicationSchema import LegalCaregiverOrGuardianCommunicationSchema

class LegalCaregiverOrGuardianSchema(BaseModel):
    data_provider_caregiver_id: str = Field(..., alias="dataProviderCaregiverId")
    relationship_to_patient: Optional[str] = Field(alias="relationshipToPatient", default=None)
    caregiver_mdm_id: Optional[str] = Field(alias="caregiverMDMId", default=None)
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    birth_date: date = Field(..., alias="birthDate")
    gender: Optional[str] = None
    preferred_language_code: Optional[str] = Field(alias="preferredLanguageCode", default=None)
    name_prefix_code: Optional[str] = Field(alias="namePrefixCode", default=None)
    name_suffix_code: Optional[str] = Field(alias="nameSuffixCode", default=None)
    middle_name: Optional[str] = Field(alias="middleName", default=None)
    address_line1: str = Field(..., alias="addressLine1")
    address_line2: Optional[str] = Field(alias="addressLine2", default=None)
    city: str
    state_or_province_code: str = Field(..., alias="stateOrProvinceCode")
    country_code: str = Field(..., alias="countryCode")
    postal_code: str = Field(..., alias="postalCode")
    enriched_indicator: Optional[str] = Field(alias="enrichedIndicator", default=None)
    communications: List[LegalCaregiverOrGuardianCommunicationSchema]