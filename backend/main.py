from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import camera_router, ticket_router, dashboard_router
from app.db.base import Base
from app.db.session import engine

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:5173",
  ],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


app.include_router(camera_router)
app.include_router(ticket_router)
app.include_router(dashboard_router)
Base.metadata.create_all(bind=engine)
