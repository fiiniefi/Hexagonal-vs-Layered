from typing import List

from src.registering.exceptions import InvalidRegistration
from src.registering.models import Student, Course


def one_course_at_time(student_courses: List[Course], course_to_sign: Course) -> None:
    datetimes = [course.date_time for course in student_courses]
    datetimes.append(course_to_sign.date_time)
    if len(datetimes) - len(set(datetimes)):
        raise InvalidRegistration(
            "Student can be registered for only one course at the same time"
        )


def should_be_on_valid_semester(student: Student, course: Course) -> None:
    if student.semester != course.semester:
        raise InvalidRegistration(
            f"Student {student.id} is on the {student.semester} semester, while"
            f"a course {course.id} should be passed on the {course.semester} semester"
        )
