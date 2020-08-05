from src.domain.models.registration import Registration, Student
from src.infrastructure.registration.repository import MongoRegistrationRepository


class RegistrationService:
    def __init__(self) -> None:
        self.registration_repo = MongoRegistrationRepository()

    def get_registration(self, course_id: str) -> Registration:
        return self.registration_repo.get_registration(course_id)

    def register_student(self, course_id: str, student: Student) -> None:
        self.registration_repo.update_registration(course_id, student)
