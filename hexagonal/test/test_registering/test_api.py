from unittest.mock import Mock

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.registering.root import registration_service
from src.registering.models import Registration
from test.test_registering.factories import student_factory
from test.test_registering.requests import get_registration, register_student


def test_get_course_registration_calls_correctly(app, api_client):
    """
    Test sprawdzający, czy warstwa prezentacji dla funkcjonalności
    pobrania rejestracji istnieje wysyłąjąc zapytanie przy wstrzykniętych
    mockowych zależnościach.
    """
    # given
    course_id = student_id = "1"
    expected_output = Registration(course_id=course_id, student_id=student_id, place=1)
    app.dependency_overrides[registration_service] = lambda: Mock(
        get_registration=Mock(return_value=expected_output)
    )

    # when
    response = get_registration(api_client, course_id, student_id)

    # then
    assert response.status_code == HTTP_200_OK
    assert Registration.parse_obj(response.json()) == expected_output


def test_register_student_calls_correctly(app, api_client):
    """
    Test sprawdzający, czy warstwa prezentacji dla funkcjonalności
    zapisu studenta na kurs istnieje wysyłąjąc zapytanie przy wstrzykniętych
    mockowych zależnościach.
    """
    # given
    place = -2
    app.dependency_overrides[registration_service] = lambda: Mock(
        register_student=Mock(return_value=place)
    )

    # when
    response = register_student(api_client, "course_id", student_factory())

    # then
    assert response.status_code == HTTP_201_CREATED
    assert response.json() == place
