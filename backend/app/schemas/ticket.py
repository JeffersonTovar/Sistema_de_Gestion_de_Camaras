from pydantic import BaseModel, Field, validator
ALLOWED_TYPES = ["Correctivo", "Preventivo"]
ALLOWED_PRIORITY = ["Crítica", "Alta", "Media", "Baja"]
class TicketCreate(BaseModel):
  camera_id: str
  type: str
  description: str = Field(min_length=5)
  priority: str

  @validator("type")
  def validate_type(cls, v):
    if v not in ALLOWED_TYPES:
      raise ValueError("Tipo inválido")
    return v

  @validator("priority")
  def validate_priority(cls, v):
    if v not in ALLOWED_PRIORITY:
      raise ValueError("Prioridad inválida")
    return v

class TicketStatusUpdate(BaseModel):
  new_status: str
