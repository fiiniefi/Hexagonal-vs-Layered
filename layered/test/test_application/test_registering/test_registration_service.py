from unittest.mock import patch, Mock

from pytest import fixture

from src.application.registering.service import RegistrationService
from test.factories import student_factory, course_factory


@fixture
def courses_repo():
    returned_course = course_factory(student_ids=[])
    return Mock(get_course=Mock(return_value=returned_course))


def test_registration_service_register_student_should_return_valid_place(courses_repo):
    # given
    course_id = "1"
    student = student_factory()
    expected_place = 1
    registrator = Mock(register=Mock(return_value=expected_place))
    validator = Mock(validate=Mock())
    with patch(
        "src.application.registering.service.MongoCoursesRepository",
        lambda: courses_repo,
    ):
        with patch(
            "src.application.registering.service.StudentValidator", lambda: validator
        ):
            with patch(
                "src.application.registering.service.Registrator", lambda: registrator
            ):

                # when
                place = RegistrationService().register_student(course_id, student)

    # then
    assert place == expected_place
    registrator.register.assert_called_once()
    validator.validate.assert_called_once()
