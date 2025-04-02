from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func, Boolean
)
from app.db.base import Base

class LegalCaregiverOrGuardianCommunication(Base):
    __tablename__ = 'legal_caregiver_or_guardian_communication'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.legal_caregiver_or_guardian.row_id'), primary_key=True)
    value = Column(String(100), primary_key=True)
    type = Column(String(50), nullable=False)
    is_primary = Column(Boolean)
    status = Column(String(50))
    created_at = Column(DateTime, server_default=func.current_timestamp())