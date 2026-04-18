from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.services.camera_service import get_cameras, create_camera
from app.schemas.camera import CameraCreate

router = APIRouter(prefix="/cameras")

@router.get("/")
def list_cameras(
  page: int = Query(1, ge=1),
  limit: int = Query(10, le=100),
  search: str = None,
  status: str = None,
  locality: str = None,
  db: Session = Depends(get_db)
):
  return get_cameras(db, page, limit, search, status, locality)

@router.post("/")
def add_camera(data: CameraCreate, db: Session = Depends(get_db)):
  return create_camera(db, data)
