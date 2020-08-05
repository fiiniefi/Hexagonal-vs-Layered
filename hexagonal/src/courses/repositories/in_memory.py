# adapter
from typing import List

from src.exceptions import NotFound
from src.courses.models import Course
from src.courses.repositories.base import CoursesRepository


class DictCoursesRepository(CoursesRepository):
    def __init__(self, courses: List[Course]) -> None:
        self.courses = {course.id: course for course in courses}

    def get_course(self, course_id: str) -> Course:
        try:
            return self.courses[course_id]
        except KeyError:
            raise NotFound(f"Course with id {course_id} has not been found")

    def get_courses(self, course_ids: List[str]) -> List[Course]:
        return [self.courses[course_id] for course_id in course_ids]

    def save_course(self, course: Course) -> None:
        self.courses.update({course.id: course})

    def save_courses(self, courses: List[Course]) -> None:
        self.courses.update({course.id: course for course in courses})
