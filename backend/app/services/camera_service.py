from sqlalchemy.orm import Session
from app.models.camera import Camera

def get_cameras(db: Session):
  return db.query(Camera).filter(Camera.deleted_at == None).all()

def create_camera(db: Session, data):
  camera = Camera(**data.dict())
  db.add(camera)
  db.commit()
  db.refresh(camera)
  return camera
