from typing import List

from pymongo.database import Database

from src.exceptions import NotFound
from src.registering.models import Registration, Student
from src.registering.repositories.registry.base import RegistrationRepository


class MongoRegistrationRepository(RegistrationRepository):
    COLLECTION_NAME = "registry"

    def __init__(self, db: Database) -> None:
        self.collection = db[self.COLLECTION_NAME]

    def get_registration(self, student_id: str, course_id: str) -> Registration:
        registration = self.collection.find_one(
            {"student_id": student_id, "course_id": course_id}, {"_id": 0}
        )
        if not registration:
            raise NotFound(f"Registration with id {course_id} has not been found")
        return Registration.parse_obj(registration)

    def get_registrations(self, student_id: str) -> List[Registration]:
        return [
            Registration.parse_obj(result)
            for result in self.collection.find({"student_id": student_id}, {"_id": 0})
        ]

    def insert(self, registration: Registration) -> None:
        self.collection.insert_one(dict(registration))
