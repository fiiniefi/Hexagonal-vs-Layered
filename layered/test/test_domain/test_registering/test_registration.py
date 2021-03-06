from unittest.mock import patch, Mock

from pytest import fixture

from src.domain.registering.registration import Registrator
from test.factories import course_factory, student_factory


@fixture
def registration_repo():
    return Mock(insert=Mock())


@fixture
def course_repo():
    return Mock(update=Mock())


def test_registrator_should_be_able_to_correctly_register_student(
    registration_repo, course_repo
):
    """
    Test logiki rejestracji studenta na kurs. Ponieważ domena jest zależna od warstw
    niższych (tu: infrastruktury), test jest zanieczyszczony nadpisaniami repozytoriów.
    """
    # given
    course = course_factory(student_ids=[])
    student = student_factory()
    with patch(
        "src.domain.registering.registration.RegistrationRepository",
        lambda: registration_repo,
    ):
        with patch(
            "src.domain.registering.registration.CoursesRepository",
            lambda: course_repo,
        ):

            # when
            place = Registrator(course).register(student)

    # then
    assert place == 1
    registration_repo.insert.assert_called_once()
    course_repo.upsert.assert_called_once()


# there's no difference in testing validator, since it establishes no communication with the layers below
