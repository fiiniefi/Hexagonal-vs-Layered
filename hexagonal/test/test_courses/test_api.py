from unittest.mock import Mock

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.courses.api.dependencies import courses_mongo_repo
from src.courses.models import Course
from test.test_courses.requests import get_course, save_course


def test_get_course_calls_correctly(app, api_client):
    # given
    expected_output = Course(id="1", name="name")
    app.dependency_overrides[courses_mongo_repo] = lambda: Mock(
        get_course=Mock(return_value=expected_output)
    )

    # when
    response = get_course(api_client, "1")

    # then
    assert response.status_code == HTTP_200_OK
    assert response.json() == dict(expected_output)


def test_save_course_calls_correctly(app, api_client):
    # given
    app.dependency_overrides[courses_mongo_repo] = lambda: Mock(save_course=Mock())

    # when
    response = save_course(api_client, "1", "name")

    # then
    assert response.status_code == HTTP_201_CREATED
