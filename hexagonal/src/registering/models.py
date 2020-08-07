from datetime import datetime
from typing import List

from pydantic import BaseModel


class Student(BaseModel):
    id: str
    first_name: str
    last_name: str
    semester: int


class Course(BaseModel):
    id: str
    name: str
    semester: int
    student_ids: List[str]
    date_time: datetime
    type: str


class Registration(BaseModel):
    student_id: str
    course_id: str
    place: int


class RegistrationResponse(BaseModel):
    course: Course
    registration: Registration
    place: int
