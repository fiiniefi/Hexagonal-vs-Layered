from pytest import raises

from src.registering.aggregates.student.aggregate import StudentValidator
from src.registering.exceptions import InvalidRegistration
from test.test_registering.factories import (
    student_factory,
    course_factory,
)


def test_attempt_to_sign_up_for_second_course_at_the_same_time_should_fail():
    """
    Test logiki walidacji sprawdzający, czy zapis studenta na drugi kurs
    odbywający się w tym samym czasie zakończy się niepowodzeniem.
    """
    # given
    course_date_time = "wt"
    student = student_factory(semester=5)
    registered_courses = [course_factory(student_ids=["1"], date_time=course_date_time)]
    course_to_sign = course_factory(student_ids=["1"], date_time=course_date_time)
    validator = StudentValidator(student, registered_courses, course_to_sign)

    # then
    with raises(InvalidRegistration):
        validator.validate()


def test_attempt_to_sign_up_for_course_from_another_semester_than_students_should_fail():
    """
    Test logiki walidacji sprawdzający, czy zapis studenta na kurs
    przypisany do niewłaściwego (innego, niż ten, na którym znajduje się obecnie student)
    semestru zakończy się niepowodzeniem.
    """
    # given
    student = student_factory(semester=5)
    registered_courses = [course_factory(student_ids=["1"])]
    course_to_sign = course_factory(student_ids=["1"], semester=6)
    validator = StudentValidator(student, registered_courses, course_to_sign)

    # then
    with raises(InvalidRegistration):
        validator.validate()


def test_all_rules_met_should_pass():
    """
    Test logiki walidacji sprawdzający, czy kiedy spełnione zostają wszystkie
    warunki zapisu, walidacja zakończy się poprawnie.
    """
    # given
    registered_course_time = "wt"
    course_to_sign_time = "pt"
    student = student_factory(semester=5)
    registered_courses = [
        course_factory(student_ids=["1"], date_time=registered_course_time)
    ]
    course_to_sign = course_factory(
        student_ids=["1"], semester=5, date_time=course_to_sign_time
    )
    validator = StudentValidator(student, registered_courses, course_to_sign)

    # then
    validator.validate()
