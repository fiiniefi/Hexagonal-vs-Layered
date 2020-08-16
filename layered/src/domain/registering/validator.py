from typing import List

from src.domain.exceptions import InvalidRegistration
from src.domain.models.courses import Course
from src.domain.models.registration import Student


"""
Miejsce w kodzie, w którym następuje walidacja studenta, usiłującego zapisać się na kurs.
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
        Wywołanie walidatorów.
        """
        one_course_at_time(self.student_courses, self.course_to_sign)
        should_be_on_valid_semester(self.student, self.course_to_sign)


def one_course_at_time(student_courses: List[Course], course_to_sign: Course) -> None:
    """
    Student może zostać zapisany tylko na jeden kurs odbywający się w tym samym czasie.
    Funkcja przyjmuje na wejściu kursy, na które student jest już zapisany oraz kurs,
    na który usiłuje się zapisać. Jeśli okaże się, że czasy się pokrywają, rzucany jest wyjątek.
    """
    datetimes = [course.date_time for course in student_courses]
    datetimes.append(course_to_sign.date_time)
    if len(datetimes) - len(set(datetimes)):
        raise InvalidRegistration(
            "Student can be registered for only one course at the same time"
        )


def should_be_on_valid_semester(student: Student, course: Course) -> None:
    """
    Student może zostać zapisany jedynie na kursy właściwe dla jego semestru.
    Jeżeli nastąpi próba zapisu na kurs przypisany do niewłaściwego semestru, rzucany jest wyjątek.
    """
    if student.semester != course.semester:
        raise InvalidRegistration(
            f"Student {student.id} is on the {student.semester} semester, while "
            f"a course {course.id} is provided for the {course.semester} semester"
        )
