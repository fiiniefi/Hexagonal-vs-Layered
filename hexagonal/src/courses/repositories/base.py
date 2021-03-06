# port
from abc import ABC, abstractmethod
from typing import List

from src.courses.models import Course


class CoursesRepository(ABC):
    """
    Interfejs repozytorium bazodanowego, a więc jego port (jednocześnie pierwotny i wtórny).
    Implementacje możemy znaleźć w plikach in_memory.py oraz mongo.py.
    """
    @abstractmethod
    def get_course(self, course_id: str) -> Course:
        pass

    @abstractmethod
    def get_courses(self, course_ids: List[str]) -> List[Course]:
        pass

    @abstractmethod
    def save_course(self, course: Course) -> None:
        pass

    @abstractmethod
    def save_courses(self, courses: List[Course]) -> None:
        pass
