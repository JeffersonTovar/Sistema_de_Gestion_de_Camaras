from sqlalchemy.orm import Session
from app.models.ticket import Ticket
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
  query = db.query(Ticket)
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
