from typing import List

from src.registering.models import Course
from src.registering.repositories.course.base import CourseRepository


class FakeCourseRepository(CourseRepository):
    def get_course(self, course_id) -> Course:
        pass

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        pass

    def update(self, course: Course) -> None:
        pass
