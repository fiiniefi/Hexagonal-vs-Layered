from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from src.courses.api.dependencies import courses_mongo_repo
from src.courses.models import Course
from src.courses.repositories.base import CoursesRepository

router = APIRouter()


@router.get("/{course_id}", status_code=HTTP_200_OK, response_model=Course)
def get_course(
    course_id: str, courses_repository: CoursesRepository = Depends(courses_mongo_repo)
) -> Course:
    return courses_repository.get_course(course_id)


@router.post("/", status_code=HTTP_201_CREATED)
def save_course(
    course_id: str,
    course_name: str,
    courses_repository: CoursesRepository = Depends(courses_mongo_repo),
) -> None:
    courses_repository.save_course(Course(id=course_id, name=course_name))
