from datetime import datetime
from typing import List

from src.registering.models import Course
from src.registering.repositories.course.base import CourseRepository


class FakeCourseRepository(CourseRepository):
    def get_course(self, course_id) -> Course:
        return Course(
            id="1",
            name="AiSD",
            semester=5,
            student_ids=[],
            date_time=datetime.now(),
            type="seminar",
        )

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        return []

    def save_course(self, course: Course) -> None:
        pass

    def update(self, course: Course) -> None:
        pass
