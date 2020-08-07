from typing import List

from src.registering.aggregates.student.rules import (
    one_course_at_time,
    should_be_on_valid_semester,
)
from src.registering.models import Student, Course


class StudentValidator:
    def __init__(
        self, student: Student, student_courses: List[Course], course_to_sign: Course
    ) -> None:
        self.student = student
        self.student_courses = student_courses
        self.course_to_sign = course_to_sign

    def validate(self) -> None:
        one_course_at_time(self.student_courses, self.course_to_sign)
        should_be_on_valid_semester(self.student, self.course_to_sign)
