from dataclasses import dataclass


@dataclass
class MongoSettings:
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_DB: str = "test_courses"
