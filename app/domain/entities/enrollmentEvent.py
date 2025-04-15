from datetime import date
from typing import Optional
from pydantic import BaseModel

class EnrollmentEvent(BaseModel):
    data_provider_transaction_id: str
    data_provider_id: str
    data_provider_patient_id: str
    marketing_campaign_source_code: Optional[str] = None
    enrollment_date: Optional[date] = None
    applicant_type: Optional[str] = None

    class Config:
        orm_mode = True