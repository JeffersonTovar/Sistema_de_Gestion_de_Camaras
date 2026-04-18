from sqlalchemy.orm import Session
from sqlalchemy import or_
from datetime import datetime
from app.models.camera import Camera
from fastapi import HTTPException


def base_query(db):
  return db.query(Camera).filter(Camera.deleted_at == None)

def get_cameras(db, page=1, limit=10, search=None, status=None, locality=None):
  query = base_query(db)
  if search:
    query = query.filter(
      Camera.id.ilike(f"%{search}%") |
      Camera.model.ilike(f"%{search}%") |
      Camera.location.ilike(f"%{search}%")
    )
  if status:
    query = query.filter(Camera.status == status)
  if locality:
    query = query.filter(Camera.locality == locality)
  total = query.count()
  data = query.offset((page - 1) * limit).limit(limit).all()
  return {
    "data": data,
    "total": total,
    "page": page,
    "limit": limit
  }

def create_camera(db, data):
  existing = db.query(Camera).filter(Camera.id == data.id).first()
  if existing:
    raise HTTPException(
      status_code=400,
      detail=f"Camara con id {data.id} ya existe."
    )
  camera = Camera(**data.dict())
  db.add(camera)
  db.commit()
  db.refresh(camera)
  return camera

def update_camera(db, camera_id, data):
  camera = db.query(Camera).filter(
    Camera.id == camera_id,
    Camera.deleted_at == None
  ).first()
  if not camera:
    raise Exception("Camera not found")
  update_data = data.dict(exclude_unset=True)
  update_data.pop("id", None)
  for key, value in update_data.items():
    setattr(camera, key, value)
  db.commit()
  db.refresh(camera)
  return camera

def soft_delete_camera(db, camera_id: str):
  camera = db.query(Camera).filter(Camera.id == camera_id).first()
  if not camera:
    raise Exception("Camera not found")
  camera.deleted_at = datetime.utcnow()
  db.commit()
  return {"message": "Camera deleted successfully"}

def restore_camera(db, camera_id: str):
  camera = db.query(Camera).filter(Camera.id == camera_id).first()
  if not camera:
    raise Exception("Camera not found")
  camera.deleted_at = None
  db.commit()
  return {"message": "Camera restored successfully"}
