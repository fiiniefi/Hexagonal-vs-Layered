from src.registering.aggregates.course.aggregate import CourseRegistry
from test.test_registering.factories import (
    student_factory,
    course_factory,
    registration_factory,
)


def course_registry(course):
    return CourseRegistry(course)


def test_course_aggregate_should_be_able_to_put_in_reserve_when_course_overloaded():
    # given
    student_id = "1"
    expected_place = -1
    course = course_factory(student_ids=["1"] * 10, type="seminar")
    registry = course_registry(course)

    # when
    result = registry.register(student_factory(id=student_id))

    # then
    course.student_ids.append(student_id)
    assert result.course == course
    assert result.registration == registration_factory(
        student_id=student_id, course_id=course.id, place=expected_place
    )
    assert result.place == expected_place


def test_course_aggregate_should_be_able_to_sign_up_for_course_when_places_are_available():
    # given
    student_id = "1"
    expected_place = 20
    course = course_factory(student_ids=["1"] * 19, type="laboratories")
    registry = course_registry(course)

    # when
    result = registry.register(student_factory(id=student_id))

    # then
    course.student_ids.append(student_id)
    assert result.course == course
    assert result.registration == registration_factory(
        student_id=student_id, course_id=course.id, place=expected_place
    )
    assert result.place == expected_place
