from abc import ABC, abstractmethod
from typing import List

from src.registering.models import Registration


class RegistrationRepository(ABC):
    @abstractmethod
    def get_registration(self, student_id: str, course_id: str) -> Registration:
        pass

    @abstractmethod
    def get_registrations(self, student_id: str) -> List[Registration]:
        pass

    @abstractmethod
    def insert(self, registration: Registration) -> None:
        pass
