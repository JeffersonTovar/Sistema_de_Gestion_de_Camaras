from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.ticket_service import create_ticket
from app.schemas.ticket import TicketCreate

router = APIRouter(prefix="/tickets")

@router.post("/")
def add_ticket(data: TicketCreate, db: Session = Depends(get_db)):
  return create_ticket(db, data)
