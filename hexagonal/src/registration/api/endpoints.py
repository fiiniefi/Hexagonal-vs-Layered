from fastapi import APIRouter
from fastapi import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.registration.api.dependencies import registration_service_v1
from src.registration.models import Registration, Student
from src.registration.services.base import RegistrationService

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Registration)
def get_course_registration(
    course_id: str,
    registration_service: RegistrationService = Depends(registration_service_v1),
) -> Registration:
    return registration_service.get_registration(course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def register_student(
    course_id: str,
    student: Student,
    registration_service: RegistrationService = Depends(registration_service_v1),
):
    registration_service.register_student(course_id, student)


@router.post("/semester", status_code=HTTP_201_CREATED)
def define_semester():
    pass
