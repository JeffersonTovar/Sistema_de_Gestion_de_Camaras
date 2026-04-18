from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from datetime import datetime

VALID_TRANSITIONS = {
  "Nuevo": ["En curso"],
  "En curso": ["Resuelto"],
  "Resuelto": []
}

def create_ticket(db: Session, data):
  ticket = Ticket(
    **data.dict(),
    status="Nuevo"
  )
  db.add(ticket)
  db.commit()
  db.refresh(ticket)
  return ticket

def change_status(db: Session, ticket: Ticket, new_status: str):
  if new_status not in VALID_TRANSITIONS[ticket.status]:
    raise Exception("Invalid transition")
  ticket.status = new_status
  if new_status == "Resuelto":
    ticket.closed_at = datetime.utcnow()
  db.commit()
  return ticket
