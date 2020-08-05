from src.registration.models import Student, Registration
from src.registration.repositories.registry.base import RegistrationRepository
from src.registration.services.base import RegistrationService


class RegistrationServiceV1(RegistrationService):
    def __init__(self, registration_repo: RegistrationRepository) -> None:
        self.registration_repo = registration_repo

    def get_registration(self, course_id: str) -> Registration:
        return self.registration_repo.get_registration(course_id)

    def register_student(self, course_id: str, student: Student) -> None:
        self.registration_repo.update_registration(course_id, student)
