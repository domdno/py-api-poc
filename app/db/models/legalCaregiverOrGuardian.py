from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func, Date
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LegalCaregiverOrGuardian(Base):
    __tablename__ = 'legal_caregiver_or_guardian'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.event.row_id'), primary_key=True)
    data_provider_caregiver_id = Column(String(30), nullable=False)
    relationship_to_patient = Column(String(50))
    caregiver_mdm_id = Column(String(14))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(255))
    preferred_language_code = Column(String(2))
    name_prefix_code = Column(String(50))
    name_suffix_code = Column(String(50))
    middle_name = Column(String(50))
    created_at = Column(DateTime, server_default=func.current_timestamp())