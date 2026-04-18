from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.camera_service import get_cameras, create_camera
from app.schemas.camera import CameraCreate

router = APIRouter(prefix="/cameras")

@router.get("/")
def list_cameras(db: Session = Depends(get_db)):
  return get_cameras(db)

@router.post("/")
def add_camera(data: CameraCreate, db: Session = Depends(get_db)):
  return create_camera(db, data)
