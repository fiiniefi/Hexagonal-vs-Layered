from pytest import fixture, raises

from src.exceptions import NotFound
from src.courses.repositories.mongo import MongoCoursesRepository
from test.test_courses.factories import course_factory


"""
Testy produkcyjnej implementacji repozytorium działającej przy użyciu MongoDB.
"""


@fixture
def courses_mongo_repo(mongo_db):
    return MongoCoursesRepository(mongo_db)


def test_courses_mongo_repo_should_be_able_to_save_course(mongo_db, courses_mongo_repo):
    """
    Test sprawdzający, czy repozytorium "potrafi" poprawnie zapisać kurs.
    """
    # given
    course = course_factory()

    # when
    courses_mongo_repo.save_course(course)

    # then
    assert list(mongo_db[courses_mongo_repo.COLLECTION_NAME].find({}, {"_id": 0})) == [
        course.dict()
    ]


def test_courses_mongo_repo_should_be_able_to_get_course(courses_mongo_repo):
    """
    Test sprawdzający, czy repozytorium "potrafi" pobrać istniejący kurs.
    """
    # given
    course_id = "1"
    course = course_factory(course_id=course_id)
    courses_mongo_repo.save_course(course)

    # when
    course_in_db = courses_mongo_repo.get_course(course_id)

    # then
    assert course_in_db == course


def test_courses_repo_get_against_empty_collection_should_raise_error(
    courses_mongo_repo,
):
    """
    Test sprawdzający, czy repozytorium "potrafi" poinformować użytkownika o braku kursu,
    do którego ten próbuje się odwołać.
    """
    with raises(NotFound):
        courses_mongo_repo.get_course("1")
