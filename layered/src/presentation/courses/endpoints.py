from fastapi import APIRouter
from fastapi.params import Body
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.domain.models.courses import Course
from src.infrastructure.courses.repository import CoursesRepository

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Course)
def get_course(
    course_id: str,
) -> Course:
    """
    Widok zwracający kurs dla podanego id kursu. Używa wstrzykniętego obiektu repozytorium z dependencies.py
    """
    return CoursesRepository().get_course(course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def save_course(
    course: Course = Body(..., embed=True),
) -> Response:
    """
    Widok służący do zapisywania kursów o parametrach podanych na wejściu.
    Używa wstrzykniętego obiektu repozytorium z dependencies.py.
    Kurs musi zawierać: id, name, semester, date_time, type.
    """
    CoursesRepository().save_course(course)
    return Response(status_code=HTTP_201_CREATED)
