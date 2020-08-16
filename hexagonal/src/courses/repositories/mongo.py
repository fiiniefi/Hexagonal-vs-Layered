# adapter
from typing import List, Any

from src.exceptions import NotFound
from src.courses.models import Course
from src.courses.repositories.base import CoursesRepository


class MongoCoursesRepository(CoursesRepository):
    """
    Implementacja portu repozytorium (adapter jednocześnie pierwotny i wtórny) odwołująca się
    do danych przechowywanych w bazie MongoDB. Jest to obecnie produkcyjna wersja repozytorium,
    tj. wszelkie operacje na bazie danych wykonywane przez system "przechodzą" przez tę implementację.
    """
    COLLECTION_NAME = "courses"

    def __init__(self, db: Any) -> None:
        """
        Konstruktor przyjmujący wstrzyknięte połączenie z bazą danych.
        """
        self.collection = db[self.COLLECTION_NAME]

    def get_course(self, course_id: str) -> Course:
        """
        Pobranie kursu z bazy danych i przedstawienie ich w formie modelu.
        """
        course = self.collection.find_one({"id": course_id})
        if not course:
            raise NotFound(f"Course with id {course_id} was not found")
        return Course.parse_obj(course)

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        course_id_filter = [{"id": course_id} for course_id in course_ids]
        return [
            Course.parse_obj(course)
            for course in self.collection.find({"$or": [course_id_filter]})
        ]

    def save_course(self, course: Course) -> None:
        """
        Wprowadzenie kursu do bazy danych.
        """
        self.collection.insert_one(course.dict())

    def save_courses(self, courses: List[Course]) -> None:
        self.collection.insert_many([course.dict() for course in courses])
