from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.camera import Camera


def get_cameras(
  db: Session,
  page: int = 1,
  limit: int = 10,
  search: str = None,
  status: str = None,
  locality: str = None
):
  query = db.query(Camera).filter(Camera.deleted_at == None)
  if search:
    query = query.filter(
      or_(
        Camera.id.ilike(f"%{search}%"),
        Camera.model.ilike(f"%{search}%"),
        Camera.location.ilike(f"%{search}%")
      )
    )
  if status:
    query = query.filter(Camera.status == status)
  if locality:
    query = query.filter(Camera.locality == locality)
  total = query.count()
  offset = (page - 1) * limit
  data = query.offset(offset).limit(limit).all()
  return {
    "data": data,
    "total": total,
    "page": page,
    "limit": limit
  }

def create_camera(db: Session, data):
  camera = Camera(**data.dict())
  db.add(camera)
  db.commit()
  db.refresh(camera)
  return camera
