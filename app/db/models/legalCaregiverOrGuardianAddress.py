from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from app.db.base import Base

class LegalCaregiverOrGuardianAddress(Base):
    __tablename__ = 'legal_caregiver_or_guardian_address'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.legal_caregiver_or_guardian.row_id'), primary_key=True)
    address_line1 = Column(String(255))
    address_line2 = Column(String(255))
    city = Column(String(255))
    state_or_province_code = Column(String(255))
    country_code = Column(String(255))
    postal_code = Column(String(255))
    enriched_indicator = Column(String(255))
    created_at = Column(DateTime, server_default=func.current_timestamp())