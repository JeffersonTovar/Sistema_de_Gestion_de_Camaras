from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.ticket_service import create_ticket
from app.schemas.ticket import TicketCreate

router = APIRouter(prefix="/tickets")


@router.get("/")
def list_tickets(
  page: int = Query(1, ge=1),
  limit: int = Query(10, le=100),
  status: str = None,
  type: str = None,
  priority: str = None,
  start_date: str = None,
  end_date: str = None,
  db: Session = Depends(get_db)
):
  return get_tickets(
    db, page, limit, status, type, priority, start_date, end_date
  )

@router.post("/")
def add_ticket(data: TicketCreate, db: Session = Depends(get_db)):
  return create_ticket(db, data)
