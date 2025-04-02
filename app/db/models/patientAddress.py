from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from app.db.base import Base

class PatientAddress(Base):
    __tablename__ = 'patient_address'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.event.row_id'), primary_key=True)
    address_line1 = Column(String(50), nullable=False)
    address_line2 = Column(String(50))
    city = Column(String(50), nullable=False)
    state_or_province_code = Column(String(3), nullable=False)
    country_code = Column(String(2), nullable=False)
    postal_code = Column(String(10), nullable=False)
    enriched_indicator = Column(String(255))
    created_at = Column(DateTime, server_default=func.current_timestamp())