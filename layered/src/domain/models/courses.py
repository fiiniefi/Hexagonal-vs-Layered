from enum import Enum
from typing import List

from pydantic import BaseModel


class CourseTypes(Enum):
    """
    Wspierane w systemie warianty kursów
    """
    laboratories = "laboratories"
    seminar = "seminar"


class Course(BaseModel):
    """
    Model kursu. Posiada identyfikator, nazwę, jest przypisany do semestru, odbywa się w konkretnym czasie,
    posiada jeden z typów udostępnianych przez CourseTypes
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
