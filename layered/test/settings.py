from dataclasses import dataclass


@dataclass
class MongoSettings:
    TEST_MONGO_HOST = "localhost"
    TEST_MONGO_PORT = 27017
    TEST_MONGO_DB = "test_db"
