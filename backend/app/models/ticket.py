from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Ticket(Base):
  __tablename__ = "tickets"

  id = Column(String(20), primary_key=True)
  camera_id = Column(String(20), ForeignKey("cameras.id"))
  type = Column(String(50))
  description = Column(Text)
  status = Column(String(50))
  priority = Column(String(50))
  opened_at = Column(DateTime, default=datetime.utcnow)
  closed_at = Column(DateTime, nullable=True)

  camera = relationship("Camera")
