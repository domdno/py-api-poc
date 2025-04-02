from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from app.db.base import Base

class ConsentPreference(Base):
    __tablename__ = 'consent_preference'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    consent_row_id = Column(Integer, ForeignKey('bronze.consent.row_id'))
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())