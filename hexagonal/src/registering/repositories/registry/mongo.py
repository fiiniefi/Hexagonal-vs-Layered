from typing import List

from pymongo.database import Database

from src.exceptions import NotFound
from src.registering.models import Registration
from src.registering.repositories.registry.base import RegistrationRepository


class MongoRegistrationRepository(RegistrationRepository):
    """
    Implementacja portu repozytorium dla rejestracji (adapter wtórny) odwołująca się do
    danych przechowywanych w bazie MongoDB. Jest to obecnie produkcyjna wersja repozytorium,
    tj. wszelkie operacje na bazie danych wykonywane przez system "przechodzą" przez tę implementację.
    """
    COLLECTION_NAME = "registry"

    def __init__(self, db: Database) -> None:
        """
        Konstruktor przyjmujący wstrzyknięte połączenie z bazą danych.
        """
        self.collection = db[self.COLLECTION_NAME]

    def get_registration(self, student_id: str, course_id: str) -> Registration:
        """
        Pobranie obiektu rejestracji z bazy i przedstawienie ich w formie modelu.
        """
        registration = self.collection.find_one(
            {"student_id": student_id, "course_id": course_id}, {"_id": 0}
        )
        if not registration:
            raise NotFound(
                f"Registration with course_id: {course_id} and student_id: {student_id} was not found"
            )
        return Registration.parse_obj(registration)

    def get_registrations(self, student_id: str) -> List[Registration]:
        return [
            Registration.parse_obj(result)
            for result in self.collection.find({"student_id": student_id}, {"_id": 0})
        ]

    def insert(self, registration: Registration) -> None:
        """
        Wprowadzenie nowo stworzonego obiektu rejestracji do bazy danych.
        """
        self.collection.insert_one(dict(registration))
