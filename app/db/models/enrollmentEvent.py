from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, Date, func
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EnrollmentEvent(Base):
    __tablename__ = 'enrollment_event'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.event.row_id'), primary_key=True)
    data_provider_transaction_id = Column(String(255), nullable=False)
    data_provider_id = Column(String(50), nullable=False)
    data_provider_patient_id = Column(String(255), nullable=False)
    marketing_campaign_source_code = Column(String(255))
    enrollment_date = Column(Date)
    applicant_type = Column(String(255))
    created_at = Column(DateTime, server_default=func.current_timestamp())