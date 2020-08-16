from pytest import fixture

from src.registering.repositories.course.mongo import MongoCourseRepository
from src.registering.repositories.registry.mongo import MongoRegistrationRepository
from src.registering.services.v1 import RegistrationServiceV1
from test.test_registering.factories import (
    course_factory,
    student_factory,
    registration_factory,
)


@fixture
def registration_repo(mongo_db):
    return MongoRegistrationRepository(mongo_db)


@fixture
def courses_repo(mongo_db):
    return MongoCourseRepository(mongo_db)


def test_register_student_should_return_valid_place(registration_repo, courses_repo):
    """
    Test przypadku użycia zapisu studenta na kurs, skomponowanego przez serwis.
    W sekcji "given" tworzone są kurs oraz student i następuje zapis kursu w bazie.
    W sekcji "when" wykonywany jest proces rejestracji, a w "then" - następuje sprawdzenie,
    czy student został zapisany w odpowiednie miejsce na liście, czy został stworzony obiekt
    rejestracji oraz czy kurs w bazie został zaktualizowany poprawnie.
    """
    # given
    course_id = "1"
    student_id = "2"
    expected_place = 1
    semester = 5
    course = course_factory(student_ids=[], id=course_id, semester=semester)
    courses_repo.upsert(course)
    student = student_factory(id=student_id, semester=semester)

    # when
    place = RegistrationServiceV1(registration_repo, courses_repo).register_student(
        course_id, student
    )

    # then
    course.student_ids.append(student_id)
    assert place == expected_place
    assert courses_repo.get_course(course_id) == course
    assert registration_repo.get_registration(
        student_id, course_id
    ) == registration_factory(
        student_id=student_id, course_id=course_id, place=expected_place
    )
