from fastapi import FastAPI
from app.api import camera_router, ticket_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

app.include_router(camera_router)
app.include_router(ticket_router)
Base.metadata.create_all(bind=engine)
