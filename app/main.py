from fastapi import FastAPI
from .database import engine
from . import models
from .routers import tables, reservation
import os

if os.getenv("ENV") != "test":
    models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tables.router)
app.include_router(reservation.router)

