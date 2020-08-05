from abc import ABC, abstractmethod

from src.registration.models import Registration, Student


class RegistrationRepository(ABC):
    @abstractmethod
    def get_registration(self, course_id: str) -> Registration:
        pass

    @abstractmethod
    def update_registration(self, course_id: str, student: Student) -> None:
        pass
