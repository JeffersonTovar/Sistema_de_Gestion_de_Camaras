from fastapi import FastAPI
from app.api import camera_router, ticket_router

app = FastAPI()

app.include_router(camera_router)
app.include_router(ticket_router)
