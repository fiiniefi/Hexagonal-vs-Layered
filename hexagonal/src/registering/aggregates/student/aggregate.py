from typing import List

from src.registering.aggregates.student.rules import (
    one_course_at_time,
    should_be_on_valid_semester,
)
from src.registering.models import Student, Course


"""
Miejsce w kodzie, w którym następuje walidacja studenta bazująca na regułach biznesowych
zdefinoiwanych w pliku rules.py.
"""


class StudentValidator:
    def __init__(
        self, student: Student, student_courses: List[Course], course_to_sign: Course
    ) -> None:
        """
        Konstruktor walidatora, przyjmujący parametry podane na wejściu.
        """
        self.student = student
        self.student_courses = student_courses
        self.course_to_sign = course_to_sign

    def validate(self) -> None:
        """
        Wywołanie walidatorów z pliku rules.py.
        """
        one_course_at_time(self.student_courses, self.course_to_sign)
        should_be_on_valid_semester(self.student, self.course_to_sign)
