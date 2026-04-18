from sqlalchemy import Column, String, Float, Date, DateTime
from app.db.base_class import Base

class Camera(Base):
  __tablename__ = "cameras"

  id = Column(String(20), primary_key=True, index=True)
  model = Column(String(255))
  location = Column(String(255))
  lat = Column(Float)
  lng = Column(Float)
  status = Column(String(50))
  locality = Column(String(100))
  last_maintenance = Column(Date)
  deleted_at = Column(DateTime, nullable=True)
