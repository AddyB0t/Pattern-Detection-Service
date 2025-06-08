from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from .database import Base

class PatternDetection(Base):
    __tablename__ = "pattern_detections"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    original_text = Column(String)
    detected_patterns = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
