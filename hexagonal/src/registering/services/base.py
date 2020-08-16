from abc import abstractmethod, ABC

from src.registering.models import Registration, Student


class RegistrationService(ABC):
    """
    Interfejs serwisu tworzącego przypadek użycia rejestracji. Razem z implementacją
    stanowi port pierwotny.
    """
    @abstractmethod
    def get_registration(self, student_id: str, course_id: str) -> Registration:
        pass

    @abstractmethod
    def register_student(self, course_id: str, student: Student) -> int:
        pass
