from pydantic import BaseModel

class TicketCreate(BaseModel):
  camera_id: str
  type: str
  description: str
  priority: str

class TicketResponse(BaseModel):
  id: str
  status: str

  class Config:
    from_attributes = True
