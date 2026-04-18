from pydantic import BaseModel

class CameraBase(BaseModel):
  model: str
  location: str
  lat: float
  lng: float
  status: str
  locality: str

class CameraCreate(CameraBase):
  id: str

class CameraResponse(CameraBase):
  id: str
  class Config:
    from_attributes = True
