from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class EnrollmentEvent(BaseModel):
    row_id: int  # FK to Event.row_id
    data_provider_transaction_id: str
    data_provider_id: str
    data_provider_patient_id: str
    marketing_campaign_source_code: Optional[str] = None
    enrollment_date: Optional[date] = None
    applicant_type: Optional[str] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True