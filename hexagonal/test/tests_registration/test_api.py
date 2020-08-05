from unittest.mock import Mock

from starlette.status import HTTP_200_OK

from src.registration.api.dependencies import registration_service_v1
from src.registration.models import Registration
from test.tests_registration.requests import get_course_registration


def test_get_course_registration_calls_correctly(app, api_client):
    # given
    course_id = "1"
    expected_output = Registration(course_id=course_id, registered_students=[])
    app.dependency_overrides[registration_service_v1] = lambda: Mock(get_registration=Mock(return_value=expected_output))

    # when
    response = get_course_registration(api_client, course_id)

    # then
    assert response.status_code == HTTP_200_OK
    assert Registration.parse_obj(response.json()) == expected_output
