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

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        course_id_filter = [{"id": course_id} for course_id in course_ids]
        return [
            Course.parse_obj(course)
            for course in self.collection.find({"$or": [course_id_filter]})
        ]

    def save_course(self, course: Course) -> None:
        self.collection.insert_one(dict(course))

    def save_courses(self, courses: List[Course]) -> None:
        self.collection.insert_many([dict(course) for course in courses])