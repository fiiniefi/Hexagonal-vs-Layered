from unittest.mock import patch

from pytest import fixture, raises

from src.exceptions import NotFound
from src.infrastructure.courses.repository import MongoCoursesRepository
from test.factories import course_factory


@fixture
def courses_repo(mongo_db):
    with patch("src.infrastructure.courses.repository.mongo_db", lambda: mongo_db):
        yield MongoCoursesRepository()


def test_courses_mongo_repo_should_be_able_to_save_course(mongo_db, courses_repo):
    # given
    course = course_factory(student_ids=[])

    # when
    courses_repo.save_course(course)

    # then
    assert list(mongo_db[courses_repo.COLLECTION_NAME].find({}, {"_id": 0})) == [
        dict(course)
    ]


def test_courses_mongo_repo_should_be_able_to_get_course(courses_repo):
    # given
    course_id = "1"
    course = course_factory(student_ids=[], id=course_id)
    courses_repo.save_course(course)

    # when
    course_in_db = courses_repo.get_course(course_id)

    # then
    assert course_in_db == course


def test_courses_repo_get_against_empty_collection_should_raise_error(courses_repo,):
    with raises(NotFound):
        courses_repo.get_course("1")
