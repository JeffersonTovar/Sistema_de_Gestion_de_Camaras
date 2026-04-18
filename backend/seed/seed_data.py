from app.models.camera import Camera
from app.models.ticket import Ticket
from datetime import datetime

def seed_cameras(db):
  cameras = [
    Camera(id=f"CAM-{str(i).zfill(3)}",
      model="Hikvision DS-2DE4425IW" if i % 2 == 0 else "Dahua IPC-HFW5442H",
      location=f"Zona {i}",
      lat=4.6 + (i * 0.01),
      lng=-74.08 - (i * 0.01),
      status="Activa" if i % 5 != 0 else "Inactiva",
      locality="Bogotá",
      last_maintenance=datetime(2025, (i % 12) + 1, (i % 27) + 1)
    )
    for i in range(1, 21)
  ]
  for cam in cameras:
    exists = db.query(Camera).filter(Camera.id == cam.id).first()
    if not exists:
      db.add(cam)
  db.commit()

def seed_tickets(db):
  tickets = [
    Ticket(
      id=f"TKT-2026-{str(i).zfill(3)}",
      camera_id=f"CAM-{str((i % 15) + 1).zfill(3)}",
      type="Correctivo" if i % 2 == 0 else "Preventivo",
      description=f"Incidencia simulada en cámara CAM-{str((i % 15) + 1).zfill(3)}",
      status="Nuevo" if i % 3 == 0 else "En curso",
      priority="Alta" if i % 4 == 0 else "Media",
      opened_at=datetime(2026, (i % 12) + 1, (i % 27) + 1),
      closed_at=None
    )
    for i in range(1, 16)
  ]

  valid_cameras = {c.id for c in db.query(Camera.id).all()}

  for tkt in tickets:
    if tkt.camera_id not in valid_cameras:
      print(f"Cámara no existe: {tkt.camera_id}")
      continue

    exists = db.query(Ticket).filter(Ticket.id == tkt.id).first()
    if not exists:
      db.add(tkt)
  db.commit()

def run_seed(db):
  seed_cameras(db)
  seed_tickets(db)
