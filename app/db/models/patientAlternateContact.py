from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PatientAlternateContact(Base):
    __tablename__ = 'patient_alternate_contact'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.event.row_id'), primary_key=True)
    full_name = Column(String(100), nullable=False)
    relationship_to_patient = Column(String(255), nullable=False)
    phone_number = Column(String(15))
    email_address = Column(String(100))
    created_at = Column(DateTime, server_default=func.current_timestamp())