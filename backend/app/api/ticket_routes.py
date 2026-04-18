from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from datetime import datetime
from app.services.ticket_service import create_ticket, get_tickets, update_ticket_status, delete_ticket
from app.schemas.ticket import TicketCreate

router = APIRouter(prefix="/tickets")


@router.get("/")
def list_tickets(
  page: int = Query(1, ge=1),
  limit: int = Query(10, le=100),
  status: str = None,
  type: str = None,
  priority: str = None,
  start_date: datetime  = None,
  end_date: datetime  = None,
  db: Session = Depends(get_db)
):
  return get_tickets(
    db, page, limit, status, type, priority, start_date, end_date
  )

@router.post("/")
def add_ticket(data: TicketCreate, db: Session = Depends(get_db)):
  return create_ticket(db, data)

@router.patch("/{ticket_id}/status")
def change_status(ticket_id: str, new_status: str, db: Session = Depends(get_db)):
  return update_ticket_status(db, ticket_id, new_status)

@router.delete("/{ticket_id}")
def remove_ticket(ticket_id: str, db: Session = Depends(get_db)):
  return delete_ticket(db, ticket_id)
