from abc import abstractmethod, ABC

from src.registration.models import Registration, Student


class RegistrationService(ABC):
    @abstractmethod
    def get_registration(self, course_id: str) -> Registration:
        pass

    @abstractmethod
    def register_student(self, course_id: str, student: Student) -> None:
        pass
