from typing import Optional

from fastapi import FastAPI
from src import routers

app = FastAPI()

app.include_router(routers.authRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}
