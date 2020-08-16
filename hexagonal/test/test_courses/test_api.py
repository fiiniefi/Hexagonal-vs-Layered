from unittest.mock import Mock

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.courses.api.dependencies import courses_mongo_repo
from src.courses.models import Course
from test.test_courses.factories import course_factory
from test.test_courses.requests import get_course, save_course


def test_get_course_calls_correctly(app, api_client):
    """
    Test sprawdzający, czy warstwa prezentacji dla funkcjonalności
    pobrania kursu istnieje wysyłąjąc zapytanie przy wstrzykniętych
    mockowych zależnościach.
    """
    # given
    expected_output = course_factory()
    app.dependency_overrides[courses_mongo_repo] = lambda: Mock(
        get_course=Mock(return_value=expected_output)
    )

    # when
    response = get_course(api_client, "1")

    # then
    assert response.status_code == HTTP_200_OK
    assert response.json() == expected_output.dict()


def test_save_course_calls_correctly(app, api_client):
    """
    Test sprawdzający, czy warstwa prezentacji dla funkcjonalności
    zapisu kursu istnieje wysyłąjąc zapytanie przy wstrzykniętych
    mockowych zależnościach.
    """
    # given
    course = course_factory()
    app.dependency_overrides[courses_mongo_repo] = lambda: Mock(save_course=Mock())

    # when
    response = save_course(api_client, course)

    # then
    assert response.status_code == HTTP_201_CREATED
