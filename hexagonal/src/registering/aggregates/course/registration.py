from dataclasses import dataclass

from src.registering.models import Student, Course, Registration


"""
Moduł zawierający logikę rejestracji studentów na kursy.
"""


@dataclass
class PlacesNumber:
    """
    Logika przechowująca informację o dostępnych miejscach w konkretnych rodzajach kursów.
    """
    laboratories: int = 20
    seminar: int = 10


class RegistrationAggregate:
    """
    Agregat odpowiedzialny za rejestrację studentów na kurs.
    """
    def __init__(self, course: Course) -> None:
        """
        Konstruktor definiujący parametry (kurs oraz rejestracja, która dopiero powstanie)
        """
        self.course = course
        self.registration = None

    def register(self, student: Student) -> int:
        """
        Zapis wskazanego poprzez parametr studenta na kurs. Polega na dodaniu identyfikatora
        tegoż studenta do listy zapisanych studentów, stworzeniu obiektu rejestracji oraz
        zwróceniu miejsca, na którym znalazł się student.
        """
        self.course.student_ids.append(student.id)
        place = self._place_on_list()

        self.registration = Registration(
            student_id=student.id, course_id=self.course.id, place=place
        )
        return place

    def _place_on_list(self) -> int:
        place = len(self.course.student_ids)
        number_of_places = getattr(PlacesNumber, self.course.type.value)
        course_overloaded = place > number_of_places
        return number_of_places - place if course_overloaded else place
