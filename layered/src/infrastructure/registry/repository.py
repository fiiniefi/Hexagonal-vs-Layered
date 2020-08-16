from src.conf.setup import mongo_db
from src.domain.models.registration import Registration
from src.exceptions import NotFound


class RegistrationRepository:
    """
    Repozytorium MongoDB dla rejestracji używane i inicjalizowane bezpośrednio przez warstwy wyższe.
    Wszelkie operacje na bazie danych wykonywane przez system "przechodzą" przez to repozytorium.
    """
    COLLECTION_NAME = "registry"

    def __init__(self) -> None:
        """
        Konstruktor repozytorium, tworzący ad hoc połączenie z bazą danych.
        Powstaje tutaj więc zależność od implementacji funkcjonalności zwracającej takie połączenie.
        """
        self.collection = mongo_db()[self.COLLECTION_NAME]

    def get_registration(self, course_id: str, student_id: str) -> Registration:
        """
        Pobranie obiektu rejestracji z bazy i przedstawienie ich w formie modelu.
        """
        registration = self.collection.find_one(
            {"course_id": course_id, "student_id": student_id}
        )
        if not registration:
            raise NotFound(
                f"Registration with id course_id: {course_id} and student_id: {student_id} was not found"
            )
        return Registration.parse_obj(registration)

    def insert(self, registration: Registration) -> None:
        """
        Wprowadzenie nowo stworzonego obiektu rejestracji do bazy danych.
        """
        self.collection.insert_one(dict(registration))
