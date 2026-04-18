from sqlalchemy import Column, String, Float, Date, DateTime
from app.db.base import Base

class Camera(Base):
  __tablename__ = "cameras"

  id = Column(String(20), primary_key=True, index=True)
  model = Column(String(255), nullable=False)
  location = Column(String(255), nullable=False)
  lat = Column(Float, nullable=False)
  lng = Column(Float, nullable=False)
  status = Column(String(50), nullable=False)
  locality = Column(String(100))
  last_maintenance = Column(Date)

  deleted_at = Column(DateTime, nullable=True)
