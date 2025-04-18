from sqlalchemy import (
    Column, Integer, String,
    DateTime, func
)
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class LandingData(Base):
    __tablename__ = 'landing_data'
    __table_args__ = {'schema': 'raw'}

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    request_method = Column(String(255))
    request_path = Column(String(255))
    request_data = Column(JSONB)
    created_at = Column(DateTime, server_default=func.current_timestamp())