from sqlalchemy import (
    Column, Integer, String, DateTime,
    ForeignKey, func
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ConsentPreferencesOption(Base):
    __tablename__ = 'consent_preferences_option'
    __table_args__ = {'schema': 'bronze'}

    row_id = Column(Integer, primary_key=True, autoincrement=True)
    consent_preference_row_id = Column(Integer, ForeignKey('bronze.consent_preference.row_id'))
    selected_option = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.current_timestamp())