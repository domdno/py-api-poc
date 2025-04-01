from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Consent(Base):
    __tablename__ = 'consent'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    patient_row_id = Column(Integer, ForeignKey('bronze.event.row_id'))
    name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())