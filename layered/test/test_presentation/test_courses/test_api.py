from unittest.mock import Mock, patch

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from test.factories import course_factory
from test.requests import get_course, save_course


def test_get_course_calls_correctly(api_client):
    # given
    course = course_factory(student_ids=[])
    courses_repo = Mock(get_course=Mock(return_value=course))
    with patch(
        "src.presentation.courses.endpoints.MongoCoursesRepository",
        lambda: courses_repo,
    ):

        # when
        response = get_course(api_client, "1")

    # then
    assert response.status_code == HTTP_200_OK
    courses_repo.get_course.assert_called_once()


def test_save_course_calls_correctly(api_client):
    # given
    courses_repo = Mock(save_course=Mock())
    with patch(
        "src.presentation.courses.endpoints.MongoCoursesRepository",
        lambda: courses_repo,
    ):
        # when
        response = save_course(api_client, "1", "AiSD")

    # then
    assert response.status_code == HTTP_201_CREATED
    courses_repo.save_course.assert_called_once()
