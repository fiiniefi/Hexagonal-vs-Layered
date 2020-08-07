from fastapi import APIRouter
from fastapi import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.registering.api.dependencies import registration_service_v1
from src.registering.models import Registration, Student
from src.registering.services.base import RegistrationService

router = APIRouter()


@router.get(
    "/{course_id}/{student_id}/", status_code=HTTP_200_OK, response_model=Registration
)
def get_registration(
    course_id: str,
    student_id: str,
    registration_service: RegistrationService = Depends(registration_service_v1),
) -> Registration:
    return registration_service.get_registration(student_id, course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def register_student(
    course_id: str,
    student: Student,
    registration_service: RegistrationService = Depends(registration_service_v1),
) -> int:
    """ When registration is successful, an endpoint returns a positive number,
        (number of a user in the group)
        Otherwise a negative number is returned, which is student's place
        in the reserve
    """
    return registration_service.register_student(course_id, student)
