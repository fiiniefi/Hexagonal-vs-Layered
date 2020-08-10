from datetime import datetime

from src.domain.models.courses import Course
from src.domain.models.registration import Student, Registration


def course_factory(
    student_ids,
    id="1",
    name="AiSD",
    semester=5,
    date_time=datetime.now(),
    type="seminar",
):
    return Course(
        student_ids=student_ids,
        id=id,
        name=name,
        semester=semester,
        date_time=date_time,
        type=type,
    )


def student_factory(id="1", first_name="First", last_name="Last", semester=5):
    return Student(id=id, first_name=first_name, last_name=last_name, semester=semester)


def registration_factory(student_id="1", course_id="1", place=1):
    return Registration(student_id=student_id, course_id=course_id, place=place)
