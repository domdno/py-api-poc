from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, Date, func, Boolean
)
from app.db.base import Base

class Patient(Base):
    __tablename__ = 'patient'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, ForeignKey('bronze.event.row_id'), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(255))
    preferred_language_code = Column(String(2))
    name_prefix_code = Column(String(50))
    name_suffix_code = Column(String(50))
    middle_name = Column(String(50))
    mdm_id = Column(String(14), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.current_timestamp())