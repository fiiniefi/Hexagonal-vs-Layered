from pymongo import MongoClient
from pymongo.database import Database

from src.conf.settings import MongoSettings


def mongo_client() -> MongoClient:
    return MongoClient(MongoSettings.MONGO_HOST, MongoSettings.MONGO_PORT)


def mongo_db() -> Database:
    return mongo_client()[MongoSettings.MONGO_DB]
