from typing import Optional
from fastapi import FastAPI

from src import routers
from src import database

database.connect_to_db()

app = FastAPI()

app.include_router(routers.authRouter, prefix="/api/auth")
