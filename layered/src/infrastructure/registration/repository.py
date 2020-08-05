from src.conf.setup import mongo_db
from src.domain.models.registration import Registration, Student
from src.exceptions import NotFound


class MongoRegistrationRepository:
    COLLECTION_NAME = "registry"

    def __init__(self) -> None:
        self.collection = mongo_db()[self.COLLECTION_NAME]

    def get_registration(self, course_id: str) -> Registration:
        registration = self.collection.find({"course_id": course_id})
        if not registration:
            raise NotFound(f"Registration with id {course_id} has not been found")
        return Registration.parse_obj(registration)

    def update_registration(self, course_id: str, student: Student) -> None:
        self.collection.update_many(
            {"course_id": course_id},
            {"$addToSet": {"registered_students": dict(student)}},
            upsert=True,
        )
