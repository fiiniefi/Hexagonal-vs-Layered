from fastapi import Depends
from pymongo.database import Database

from src.conf.setup import mongo_db
from src.registration.repositories.registry.mongo import MongoRegistrationRepository
from src.registration.services.v1 import RegistrationServiceV1


def registration_service_v1(db: Database = Depends(mongo_db)):
    return RegistrationServiceV1(MongoRegistrationRepository(db))
