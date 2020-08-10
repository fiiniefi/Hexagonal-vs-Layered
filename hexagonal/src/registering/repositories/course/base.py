from abc import ABC, abstractmethod
from typing import List

from src.registering.models import Course


class CourseRepository(ABC):
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
    def update(self, course: Course) -> None:
        pass
