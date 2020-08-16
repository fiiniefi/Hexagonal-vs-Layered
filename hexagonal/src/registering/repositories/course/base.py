from abc import ABC, abstractmethod
from typing import List

from src.registering.models import Course


class CourseRepository(ABC):
    """
    Interfejs repozytorium bazodanowego (dla kursów w kontekście rejestracji),
    a więc jego port wtórny. Implementacje możemy znaleźć w plikach fake.py oraz mongo.py.
    """
    @abstractmethod
    def get_course(self, course_id: str) -> Course:
        pass

    @abstractmethod
    def get_courses(self, course_ids: List[str]) -> List[Course]:
        pass

    @abstractmethod
    def upsert(self, course: Course) -> None:
        pass
