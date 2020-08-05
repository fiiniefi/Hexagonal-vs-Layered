from pytest import fixture, raises

from src.exceptions import NotFound
from src.courses.repositories.in_memory import DictCoursesRepository
from test.test_courses.factories import course_factory


@fixture
def courses_in_memory_repo(mongo_db):
    return DictCoursesRepository([])


def test_courses_mongo_repo_should_be_able_to_save_course(
    courses_in_memory_repo
):
    # given
    course = course_factory()

    # when
    courses_in_memory_repo.save_course(course)

    # then
    assert courses_in_memory_repo.courses[course.id] == course


def test_courses_mongo_repo_should_be_able_to_get_course(courses_in_memory_repo):
    # given
    course_id = "1"
    course = course_factory(course_id=course_id)
    courses_in_memory_repo.save_course(course)

    # when
    course_in_db = courses_in_memory_repo.get_course(course_id)

    # then
    assert course_in_db == course


def test_courses_repo_get_against_empty_collection_should_raise_error(
    courses_in_memory_repo,
):
    with raises(NotFound):
        courses_in_memory_repo.get_course("1")
