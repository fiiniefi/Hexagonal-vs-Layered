from unittest.mock import Mock, patch

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from test.factories import course_factory
from test.requests import get_course, save_course


"""
Testy warstwy prezentacji dla funkcjonalności z courses.
Ponieważ w architekturze warstwowej nie ma portów i adapterów, testy
podstawiają mocka za zależność w postaci repozytorium Courses.
Sprawdzają jedynie, czy warstwa prezentacji działa poprawnie w oderwaniu
od reszty implementacji funkcjonalności.
"""


def test_get_course_calls_correctly(api_client):
    # given
    course = course_factory(student_ids=[])
    courses_repo = Mock(get_course=Mock(return_value=course))
    with patch(
        "src.presentation.courses.endpoints.CoursesRepository",
        lambda: courses_repo,
    ):

        # when
        response = get_course(api_client, "1")

    # then
    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(course)


def test_save_course_calls_correctly(api_client):
    # given
    courses_repo = Mock(save_course=Mock())
    with patch(
        "src.presentation.courses.endpoints.CoursesRepository",
        lambda: courses_repo,
    ):
        # when
        response = save_course(api_client, "1", "AiSD")

    # then
    assert response.status_code == HTTP_201_CREATED
