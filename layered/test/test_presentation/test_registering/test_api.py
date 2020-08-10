from unittest.mock import patch, Mock

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from test.factories import registration_factory, student_factory
from test.requests import get_registration, register_student


def test_get_course_registration_calls_correctly(api_client):
    # given
    registration = registration_factory()
    registration_service = Mock(get_registration=Mock(return_value=registration))
    with patch(
        "src.presentation.registering.endpoints.RegistrationService",
        lambda: registration_service,
    ):

        # when
        response = get_registration(api_client, "1", "1")

    # then
    assert response.status_code == HTTP_200_OK
    registration_service.get_registration.assert_called_once()


def test_register_student_calls_correctly(api_client):
    # given
    place = 1
    registration_service = Mock(register_student=Mock(return_value=place))
    with patch(
        "src.presentation.registering.endpoints.RegistrationService",
        lambda: registration_service,
    ):
        # when
        response = register_student(api_client, "1", student_factory())

    # then
    assert response.status_code == HTTP_201_CREATED
    registration_service.register_student.assert_called_once()
