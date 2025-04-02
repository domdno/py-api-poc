from sqlalchemy import (
    Column, Integer, String, DateTime,
    UniqueConstraint
)
from app.db.base import Base

class Event(Base):
    __tablename__ = 'event'
    __table_args__ = (
        UniqueConstraint('event_type', 'version', 'created_timestamp', 'request_id', name='uq_event'),
        {'schema': 'bronze'}
    )

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    event_type = Column(String(50), nullable=False)
    version = Column(String(255), nullable=False)
    created_timestamp = Column(DateTime, nullable=False)
    request_id = Column(String(255))