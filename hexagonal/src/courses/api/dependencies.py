from fastapi import Depends
from pymongo.database import Database

from src.conf.setup import mongo_db
from src.courses.repositories.mongo import MongoCoursesRepository


def courses_mongo_repo(db: Database = Depends(mongo_db)) -> MongoCoursesRepository:
    """
    Inicjalizacja adaptera repozytorium w implementacji Mongo. Przyjmuje wstrzyknięte
    połączenie z bazą danych.
    """
    return MongoCoursesRepository(db)
