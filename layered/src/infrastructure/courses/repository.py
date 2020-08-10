from typing import List

from src.conf.setup import mongo_db
from src.domain.models.courses import Course
from src.exceptions import NotFound


class MongoCoursesRepository:
    COLLECTION_NAME = "test_courses"

    def __init__(self) -> None:
        self.collection = mongo_db()[self.COLLECTION_NAME]

    def get_course(self, course_id: str) -> Course:
        course = self.collection.find_one({"id": course_id})
        if not course:
            raise NotFound(f"Course with id {course_id} has not been found")
        return Course.parse_obj(course)

    def get_courses(self) -> List[Course]:
        return [Course.parse_obj(course) for course in self.collection.find()]

    def save_course(self, course: Course) -> None:
        self.collection.insert_one(dict(course))

    def save_courses(self, courses: List[Course]) -> None:
        self.collection.insert_many([dict(course) for course in courses])

    def update(self, course: Course) -> None:
        pass
