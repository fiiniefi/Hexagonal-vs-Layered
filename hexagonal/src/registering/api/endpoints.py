from fastapi import APIRouter
from fastapi import Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.registering.models import Registration, Student
from src.registering.root import registration_service
from src.registering.services.base import RegistrationService

router = APIRouter()


@router.get(
    "/{course_id}/{student_id}/", status_code=HTTP_200_OK, response_model=Registration
)
def get_registration(
    course_id: str,
    student_id: str,
    service: RegistrationService = Depends(registration_service),
) -> Registration:
    """
    Widok zwracający obiekt rejestracji dla podanych identyfikatorów kursu oraz studenta.
    Używa wstrzykniętego obiektu serwisu z dependencies.py
    """
    return service.get_registration(student_id, course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def register_student(
    course_id: str,
    student: Student,
    service: RegistrationService = Depends(registration_service),
) -> int:
    """
    Widok odpowiadający za rejestrację studenta o parametrach podanych na wejściu
    na kurs o identyfikatorze również podanym na wejściu.
    Używa wstrzykniętego obiektu serwisu z dependencies.py
    ___________________________________________________________________
    When registering is successful, an endpoint returns a positive number,
    (number of a user in the group)
    Otherwise a negative number is returned, which is student's place
    in the reserve
    """
    return service.register_student(course_id, student)
