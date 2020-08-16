from dataclasses import dataclass

from src.domain.models.courses import Course
from src.domain.models.registration import Student, Registration
from src.infrastructure.courses.repository import CoursesRepository
from src.infrastructure.registry.repository import RegistrationRepository


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


class Registrator:
    """
    Klasa odpowiedzialna za rejestrację studentów na kurs.
    """
    def __init__(self, course: Course) -> None:
        """
        Konstruktor definiujący parametry klasy. Wśród nich znajdują się:
        - podany na wejściu kurs
        - stworzona ad hoc implementacja repozytorium Registration
        - stworzona ad hoc implementacja repozytorium Courses
        Jak można zauważyć, powstają tutaj zależności domeny od definiowanych repozytoriów.
        W przeciwieństwie do implementacji heksagonalnej, tutaj takie podejście nie narusza
        żadnej istotnej zasady - warstwa infrastruktury, z której pochodzą repozytoria znajduje się
        "poniżej" domenowej.
        """
        self.course = course
        self.registration_repo = RegistrationRepository()
        self.course_repo = CoursesRepository()

    def register(self, student: Student) -> int:
        """
        Zapis wskazanego poprzez parametr studenta na kurs. Polega na dodaniu identyfikatora
        tegoż studenta do listy zapisanych studentów, stworzeniu obiektu rejestracji,
        zapisie rejestracji oraz zaktualizowanego kursu w bazie danych oraz
        zwróceniu miejsca, na którym znalazł się student.
        """
        self.course.student_ids.append(student.id)
        place = self._place_on_list()

        registration = Registration(
            student_id=student.id, course_id=self.course.id, place=place
        )
        self.registration_repo.insert(registration)
        self.course_repo.upsert(self.course)
        return place

    def _place_on_list(self) -> int:
        place = len(self.course.student_ids)
        number_of_places = getattr(PlacesNumber, self.course.type.value)
        course_overloaded = place > number_of_places
        return number_of_places - place if course_overloaded else place
