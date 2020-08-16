from datetime import datetime
from typing import List

from src.registering.models import Course
from src.registering.repositories.course.base import CourseRepository


class FakeCourseRepository(CourseRepository):
    """
    Implementacja portu repozytorium (adapter wtórny) "udająca" działanie. Nie przechowuje danych nigdzie.
    Jej użytecznosć sprowadza się jedynie do testów - robi za "fałszywkę".
    """
    def get_course(self, course_id) -> Course:
        return Course(
            id="1",
            name="AiSD",
            semester=5,
            student_ids=[],
            date_time="wt",
            type="seminar",
        )

    def get_courses(self, _: List[str]) -> List[Course]:
        return []

    def upsert(self, course: Course) -> None:
        pass
