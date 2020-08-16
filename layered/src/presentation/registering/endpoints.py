from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.application.registering.service import RegistrationService
from src.domain.models.registration import Registration, Student

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Registration)
def get_course_registration(course_id: str, student_id: str) -> Registration:
    """
    Widok zwracający obiekt rejestracji dla podanych identyfikatorów kursu oraz studenta.
    Tworzy obiekt serwisu ad hoc i używa go w celu pobrania rejestracji.
    """
    return RegistrationService().get_registration(course_id, student_id)


@router.post("/", status_code=HTTP_201_CREATED)
def register_student(course_id: str, student: Student) -> int:
    """
    Widok odpowiadający za rejestrację studenta o parametrach podanych na wejściu
    na kurs o identyfikatorze również podanym na wejściu.
    Tworzy obiekt serwisu ad hoc i używa go w celu dokonania rejestracji.
    """
    return RegistrationService().register_student(course_id, student)
