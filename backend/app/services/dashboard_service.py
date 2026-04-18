from sqlalchemy.orm import Session
from app.models.camera import Camera
from app.models.ticket import Ticket
from sqlalchemy import func
from datetime import datetime

def get_dashboard_data(db: Session):

  active_cameras = db.query(Camera).filter(
    Camera.status == "Activa",
    Camera.deleted_at == None
  ).count()

  open_tickets = db.query(Ticket).filter(
    Ticket.status.in_(["Nuevo", "En curso"]),
    Ticket.deleted_at == None
  ).count()

  critical_tickets = db.query(Ticket).filter(
    Ticket.priority.in_(["Crítica", "Alta"]),
    Ticket.status.in_(["Nuevo", "En curso"]),
    Ticket.deleted_at == None
  ).count()

  resolved = db.query(Ticket).filter(
    Ticket.status == "Resuelto",
    Ticket.closed_at != None
  ).all()

  avg_days = 0
  if resolved:
    total_days = sum(
      (t.closed_at - t.opened_at).days for t in resolved
    )
    avg_days = round(total_days / len(resolved), 2)

  camera_status = db.query(
    Camera.status,
    func.count(Camera.id)
  ).filter(Camera.deleted_at == None).group_by(Camera.status).all()

  camera_status_data = [
    {"name": s, "value": c} for s, c in camera_status
  ]

  tickets_priority = db.query(
    Ticket.priority,
    func.count(Ticket.id)
  ).filter(Ticket.deleted_at == None).group_by(Ticket.priority).all()

  tickets_priority_data = [
    {"name": p, "value": c} for p, c in tickets_priority
  ]

  return {
    "kpis": {
      "activeCameras": active_cameras,
      "openTickets": open_tickets,
      "criticalTickets": critical_tickets,
      "avgResolutionTime": avg_days
    },
    "cameraStatus": camera_status_data,
    "ticketsPriority": tickets_priority_data
  }
