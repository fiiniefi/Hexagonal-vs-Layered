from typing import List

from pymongo.database import Database

from src.exceptions import NotFound
from src.registering.models import Course
from src.registering.repositories.course.base import CourseRepository


class MongoCourseRepository(CourseRepository):
    """
    Implementacja portu repozytorium (adapter wtórny) odwołująca się do danych przechowywanych w bazie MongoDB.
    Jest to obecnie produkcyjna wersja repozytorium, tj. wszelkie operacje na bazie danych
    wykonywane przez system dla kursów w kontekście rejestracji "przechodzą" przez tę implementację.
    """
    COLLECTION_NAME = "courses"

    def __init__(self, db: Database) -> None:
        """
        Konstruktor przyjmujący wstrzyknięte połączenie z bazą danych.
        """
        self.collection = db[self.COLLECTION_NAME]

    def get_course(self, course_id: str) -> Course:
        """
        Pobranie kursu z bazy danych i przedstawienie ich w formie modelu.
        """
        course = self.collection.find_one({"id": course_id}, {"_id": 0})
        if not course:
            raise NotFound(f"Course {course_id} was not found")
        return Course.parse_obj(course)

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        query = [{"id": course_id} for course_id in course_ids]
        return [
            Course.parse_obj(course)
            for course in self.collection.find({"$or": query}, {"_id": 0})
        ]

    def upsert(self, course: Course) -> None:
        """
        Aktualizacja kursu po zmianach spowodowanych rejestracją.
        """
        self.collection.update({"id": course.id}, course.dict(), upsert=True)
