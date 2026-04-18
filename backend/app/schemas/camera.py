from pydantic import BaseModel, Field, validator
ALLOWED_STATUS = ["Activa", "Inactiva", "En Mantenimiento"]

class CameraBase(BaseModel):
  model: str = Field(min_length=3, max_length=255)
  location: str = Field(min_length=3, max_length=255)
  lat: float
  lng: float
  status: str
  locality: str

  @validator("lat")
  def validate_lat(cls, v):
    if v < 4.4 or v > 4.9:
      raise ValueError("Latitud fuera de rango Bogotá (4.4 - 4.9)")
    return v

  @validator("lng")
  def validate_lng(cls, v):
    if v < -74.3 or v > -73.9:
      raise ValueError("Longitud fuera de rango Bogotá (-74.3 a -73.9)")
    return v

  @validator("status")
  def validate_status(cls, v):
    if v not in ALLOWED_STATUS:
      raise ValueError(f"Estado inválido. Permitidos: {ALLOWED_STATUS}")
    return v

class CameraCreate(CameraBase):
  id: str

class CameraResponse(CameraBase):
  id: str
  class Config:
    from_attributes = True
