from pytest import fixture

from src.registering.repositories.registry.mongo import MongoRegistrationRepository


@fixture
def registration_mongo_repo(mongo_db):
    return MongoRegistrationRepository(mongo_db)
