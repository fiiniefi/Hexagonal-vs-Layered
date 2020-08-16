from unittest.mock import Mock

from src.mailing.services.base import BaseMailingService
from src.registering.aggregates.course.registration import RegistrationAggregate
from src.registering.models import Student, Registration
from src.registering.repositories.course.base import CourseRepository
from src.registering.repositories.registry.base import RegistrationRepository
from src.registering.services.base import RegistrationService

from src.registering.aggregates.student.aggregate import StudentValidator


class RegistrationServiceV1(RegistrationService):
    """
    Serwis tworzący przypadek użycia rejestracji. Razem z interfejsem stanowi port
    pierwotny.
    """
    def __init__(
        self,
        registration_repo: RegistrationRepository,
        course_repo: CourseRepository,
        mailing_service: BaseMailingService,
    ) -> None:
        """
        Konstruktor serwisu przyjmujący wstrzyknięte repozytoria Registration oraz Course,
        a także serwis do wysyłania maili.
        """
        self.registration_repo = registration_repo
        self.course_repo = course_repo
        self.mailing_service = mailing_service

    def get_registration(self, student_id: str, course_id: str) -> Registration:
        """
        Wywołanie metody repozytorium, zwracającej obiekt rejestracji.
        """
        return self.registration_repo.get_registration(student_id, course_id)

    def register_student(self, course_id: str, student: Student) -> int:
        """
        Skomponowany przypadek użycia zapisu studenta na kurs. Przyjmuje identyfikator
        kursu oraz dane studenta do zapisu. Wykonuje walidację na agregacie studenta
        udostępnianym przez domenę. Dokonuje się tutaj operacja zapisu na agregacie
        kursu udostępnianym przez domenę. Na końcu stan agregatu kursu zapisywany jest
        w bazie danych, jako że doszło do jego zmiany.
        """
        course_to_sign = self.course_repo.get_course(course_id)
        student_registrations = self.registration_repo.get_registrations(student.id)
        student_courses = (
            self.course_repo.get_courses(
                [registration.course_id for registration in student_registrations]
            )
            if student_registrations
            else []
        )
        StudentValidator(student, student_courses, course_to_sign).validate()
        aggregate = RegistrationAggregate(course_to_sign)
        place = aggregate.register(student)

        self.registration_repo.insert(aggregate.registration)
        self.course_repo.upsert(aggregate.course)
        self._send_email()
        return place

    def _send_email(self) -> None:
        self.mailing_service.send(
            sender=Mock(),
            password=Mock(),
            receiver=Mock(),
            subject="Registration Successful",
            body=Mock(),
        )
