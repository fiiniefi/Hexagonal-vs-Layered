from fastapi import APIRouter, Depends
from fastapi.params import Body
from starlette.responses import Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.courses.api.dependencies import courses_mongo_repo
from src.courses.models import Course
from src.courses.repositories.base import CoursesRepository

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Course)
def get_course(
    course_id: str, courses_repository: CoursesRepository = Depends(courses_mongo_repo)
) -> Course:
    """
    Widok zwracający kurs dla podanego id kursu. Używa wstrzykniętego obiektu repozytorium z dependencies.py
    """
    return courses_repository.get_course(course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def save_course(
    course: Course = Body(..., embed=True),
    courses_repository: CoursesRepository = Depends(courses_mongo_repo),
) -> Response:
    """
    Widok służący do zapisywania kursów o parametrach podanych na wejściu.
    Używa wstrzykniętego obiektu repozytorium z dependencies.py.
    Kurs musi zawierać: id, name, semester, date_time, type.
    """
    courses_repository.save_course(course)
    return Response(status_code=HTTP_201_CREATED)
