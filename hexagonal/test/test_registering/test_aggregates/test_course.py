from src.registering.aggregates.course.registration import RegistrationAggregate
from test.test_registering.factories import (
    student_factory,
    course_factory,
    registration_factory,
)


def registration_aggregate(course):
    return RegistrationAggregate(course)


def test_course_aggregate_should_be_able_to_put_in_reserve_when_course_overloaded():
    """
    Test logiki agregatu zapisującego studenta na kurs. Ten przypadek testowy sprawdza, czy
    agregat poprawnie umieszcza studentów na liście rezerwowej. Przyjmuje stworzony w sekcji
    "given" kurs, następnie w sekcji "when" wykonuje operację zapisu na stworzonym ad hoc
    obiekcie studenta. W sekcji "then" następuje weryfikacja, czy agregat rejestracji
    został poprawnie zaktualizowany oraz czy zwrócił odpowiednie miejsce w kolejce.
    """
    # given
    student_id = "1"
    expected_place = -1
    course = course_factory(student_ids=["1"] * 10, type="seminar")
    aggregate = registration_aggregate(course)

    # when
    place = aggregate.register(student_factory(id=student_id))

    # then
    course.student_ids.append(student_id)
    assert aggregate.course == course
    assert aggregate.registration == registration_factory(
        student_id=student_id, course_id=course.id, place=expected_place
    )
    assert place == expected_place


def test_course_aggregate_should_be_able_to_correctly_register_student():
    """
    Test logiki agregatu zapisującego studenta na kurs. Ten przypadek testowy sprawdza, czy
    agregat poprawnie umieszcza studentów na głównej liście uczestników. Przyjmuje stworzony w sekcji
    "given" kurs, następnie w sekcji "when" wykonuje operację zapisu na stworzonym ad hoc
    obiekcie studenta. W sekcji "then" następuje weryfikacja, czy agregat rejestracji
    został poprawnie zaktualizowany oraz czy zwrócił odpowiednie miejsce w kolejce.
    """
    # given
    student_id = "1"
    expected_place = 20
    course = course_factory(student_ids=["1"] * 19, type="laboratories")
    aggregate = registration_aggregate(course)

    # when
    place = aggregate.register(student_factory(id=student_id))

    # then
    course.student_ids.append(student_id)
    assert aggregate.course == course
    assert aggregate.registration == registration_factory(
        student_id=student_id, course_id=course.id, place=expected_place
    )
    assert place == expected_place
