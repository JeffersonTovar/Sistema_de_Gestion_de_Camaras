from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.models.camera import Camera
from datetime import datetime

VALID_TRANSITIONS = {
  "Nuevo": ["En curso"],
  "En curso": ["Resuelto"],
  "Resuelto": []
}

def get_tickets(
  db: Session,
  page: int = 1,
  limit: int = 10,
  status: str = None,
  type: str = None,
  priority: str = None,
  start_date = None,
  end_date = None
):
  query = db.query(Ticket).filter(Ticket.deleted_at == None)
  if status:
    query = query.filter(Ticket.status == status)
  if type:
    query = query.filter(Ticket.type == type)
  if priority:
    query = query.filter(Ticket.priority == priority)
  if start_date:
    query = query.filter(Ticket.opened_at >= start_date)
  if end_date:
    query = query.filter(Ticket.opened_at <= end_date)
  total = query.count()
  offset = (page - 1) * limit
  data = query.offset(offset).limit(limit).all()

  return {
    "data": data,
    "total": total,
    "page": page,
    "limit": limit
  }

def create_ticket(db, data):
  camera = validate_camera_exists(db, data.camera_id)
  if camera.status == "Inactiva":
    raise Exception("Cannot create ticket for inactive camera")
  ticket = Ticket(
    **data.dict(),
    status="Nuevo"
  )
  db.add(ticket)
  db.commit()
  db.refresh(ticket)
  return ticket

def update_ticket_status(db, ticket_id, new_status):
  ticket = db.query(Ticket).filter(
    Ticket.id == ticket_id,
    Ticket.deleted_at == None
  ).first()
  if not ticket:
    raise Exception("Ticket not found")
  allowed = VALID_TRANSITIONS.get(ticket.status, [])
  if new_status not in allowed:
    raise Exception(
      f"Invalid transition {ticket.status} → {new_status}"
    )
  ticket.status = new_status
  if new_status == "Resuelto":
    ticket.closed_at = datetime.utcnow()
  db.commit()
  db.refresh(ticket)
  return ticket

def delete_ticket(db, ticket_id):
  ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
  if not ticket:
    raise Exception("Ticket not found")
  ticket.deleted_at = datetime.utcnow()
  db.commit()
  return {"message": "Ticket deleted"}


def validate_camera_exists(db, camera_id):
  camera = db.query(Camera).filter(
    Camera.id == camera_id,
    Camera.deleted_at == None
  ).first()
  if not camera:
    raise Exception("Camera not found or deleted")
  return camera
