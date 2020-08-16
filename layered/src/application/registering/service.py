from unittest.mock import Mock

from src.application.mailing.fake_service import FakeMailingService
from src.domain.models.registration import Registration, Student
from src.domain.registering.registration import Registrator
from src.domain.registering.validator import StudentValidator
from src.infrastructure.courses.repository import CoursesRepository
from src.infrastructure.registry.repository import RegistrationRepository


class RegistrationService:
    """
    Serwis tworzący przypadek użycia rejestracji.
    """
    def __init__(self) -> None:
        """
        Konstruktor serwisu tworzący ad hoc obiekty repozytoriów Registration oraz Courses.
        Powstaje tutaj więc zależność od implementacji repozytoriów.
        """
        self.registration_repo = RegistrationRepository()
        self.courses_repo = CoursesRepository()

    def get_registration(self, course_id: str, student_id: str) -> Registration:
        """
        Wywołanie metody repozytorium, zwracającej obiekt rejestracji.
        """
        return self.registration_repo.get_registration(course_id, student_id)

    def register_student(self, course_id: str, student: Student) -> int:
        """
        Skomponowany przypadek użycia zapisu studenta na kurs. Przyjmuje identyfikator
        kursu oraz dane studenta do zapisu. Wykonuje walidację na agregacie studenta
        udostępnianym przez domenę. Dokonuje się tutaj operacja zapisu na agregacie
        kursu udostępnianym przez domenę. Żadne dane ine są zapisywane w bazie,
        ponieważ zajmuje się tym warstwa domeny.
        """
        courses = self.courses_repo.get_courses()
        student_courses = [
            course for course in courses if student.id in course.student_ids
        ]
        course_to_sign = self.courses_repo.get_course(course_id)
        StudentValidator(student, student_courses, course_to_sign).validate()
        place = Registrator(course_to_sign).register(student)
        self._send_email()
        return place

    @staticmethod
    def _send_email() -> None:
        FakeMailingService().send(
            sender=Mock(),
            password=Mock(),
            receiver=Mock(),
            subject="Registration Successful",
            body=Mock(),
        )
