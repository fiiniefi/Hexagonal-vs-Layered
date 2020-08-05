from fastapi import APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.domain.models.courses import Course
from src.infrastructure.courses.repository import MongoCoursesRepository

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Course)
def get_course(
    course_id: str,
) -> Course:
    return MongoCoursesRepository().get_course(course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def save_course(
    course_id: str,
    course_name: str,
) -> None:
    MongoCoursesRepository().save_course(Course(id=course_id, name=course_name))
