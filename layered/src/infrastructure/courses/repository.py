from typing import List

from src.conf.setup import mongo_db
from src.domain.models.courses import Course
from src.exceptions import NotFound


class CoursesRepository:
    """
    Repozytorium MongoDB dla kursów używane i inicjalizowane bezpośrednio przez warstwy wyższe.
    Wszelkie operacje na bazie danych wykonywane przez system "przechodzą" przez to repozytorium.
    """
    COLLECTION_NAME = "courses"

    def __init__(self) -> None:
        """
        Konstruktor repozytorium, tworzący ad hoc połączenie z bazą danych.
        Powstaje tutaj więc zależność od implementacji funkcjonalności zwracającej takie połączenie.
        """
        self.collection = mongo_db()[self.COLLECTION_NAME]

    def get_course(self, course_id: str) -> Course:
        """
        Pobranie kursu z bazy danych i przedstawienie ich w formie modelu.
        """
        course = self.collection.find_one({"id": course_id})
        if not course:
            raise NotFound(f"Course with id {course_id} was not found")
        return Course.parse_obj(course)

    def get_courses(self, course_ids: List[str] = None) -> List[Course]:
        query = (
            {"$or": [{"id": course_id} for course_id in course_ids]}
            if course_ids
            else {}
        )
        return [Course.parse_obj(course) for course in self.collection.find(query)]

    def save_course(self, course: Course) -> None:
        """
        Wprowadzenie kursu do bazy danych.
        """
        self.collection.insert_one(course.dict())

    def save_courses(self, courses: List[Course]) -> None:
        self.collection.insert_many([course.dict() for course in courses])

    def upsert(self, course: Course) -> None:
        self.collection.update({"id": course.id}, course.dict(), upsert=True)
