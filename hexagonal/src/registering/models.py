from enum import Enum
from typing import List

from pydantic import BaseModel


"""
Zauważmy, że niektóre modele są powtórzone, a Course ma dodaną listę studentów.
To dlatego, że pojęcia te są redefiniowane w obrębie innego, niezależnego heksagonu.
"""


class Student(BaseModel):
    """
    Model studenta. Zawiera identyfikator, imię, nazwisko oraz jest przypisany do semestru.
    """
    id: str
    first_name: str
    last_name: str
    semester: int


class CourseTypes(Enum):
    """
    Wspierane w systemie warianty kursów
    """
    laboratories = "laboratories"
    seminar = "seminar"


class Course(BaseModel):
    """
    Model kursu w kontekście rejestracji. Posiada identyfikator, nazwę, jest przypisany do semestru,
    odbywa się w konkretnym czasie, posiada jeden z typów udostępnianych przez CourseTypes
    """
    id: str
    name: str
    semester: int
    student_ids: List[str] = []
    date_time: str
    type: CourseTypes

    def dict(self, *args, **kwargs) -> dict:
        course = super().dict(*args, **kwargs)
        course["type"] = course["type"].value
        return course


class Registration(BaseModel):
    """
    Model rejestracji. Przechowuje identyfikatory studenta oraz kursu i miejsce studenta na liście.
    """
    student_id: str
    course_id: str
    place: int
