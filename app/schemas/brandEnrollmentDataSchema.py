from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel, Field

from app.schemas.patientSchema import PatientSchema
from app.schemas.consentSchema import ConsentSchema

class BrandEnrollmentDataSchema(BaseModel):
    patient: PatientSchema
    consent: List[ConsentSchema] = Field(..., alias="consentsAndPreferences")
    data_provider_transaction_id: str = Field(..., alias="dataProviderTransactionId")
    data_provider_id: str = Field(..., alias="dataProviderId")
    data_provider_patient_id: str = Field(..., alias="dataProviderPatientId")
    marketing_campaign_source_code: Optional[str] = Field(alias="marketingCampaignSourceCode", default=None)
    enrollment_date: Optional[date] = Field(alias="enrollmentDate", default=None)
    applicant_type: Optional[str] = Field(alias="applicantType", default=None)