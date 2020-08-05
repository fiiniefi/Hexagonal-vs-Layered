from pymongo import MongoClient
from pytest import fixture
from starlette.testclient import TestClient

from src.app import APIBuilder
from test.settings import MongoSettings


@fixture
def app():
    return APIBuilder().build()


@fixture
def api_client(app):
    return TestClient(app)


@fixture
def mongo_client():
    return MongoClient(MongoSettings.TEST_MONGO_HOST, MongoSettings.TEST_MONGO_PORT)


@fixture
def mongo_db(mongo_client):
    mongo_client.drop_database(MongoSettings.TEST_MONGO_DB)
    yield mongo_client[MongoSettings.TEST_MONGO_DB]
