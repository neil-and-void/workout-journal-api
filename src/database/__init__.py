from mongoengine import connect
from src.config import config

def connect_to_db():
    connect(host=config.DATABASE_URL)
