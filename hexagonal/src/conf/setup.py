from pymongo import MongoClient
from pymongo.database import Database

from src.conf.settings import MongoSettings


def mongo_client() -> MongoClient:
    """
    Połączenie z serwerem MongoDB
    """
    return MongoClient(
        f"mongodb://{MongoSettings.MONGO_HOST}:{MongoSettings.MONGO_PORT}/"
    )


def mongo_db() -> Database:
    return mongo_client()[MongoSettings.MONGO_DB]
