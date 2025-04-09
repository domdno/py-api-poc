from sqlalchemy import (
    Column, Integer
)
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class ApiRequestResponse(Base):
    __tablename__ = 'api_request_response'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    request_data = Column(JSONB)
    response_data = Column(JSONB)