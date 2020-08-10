from typing import List

from pydantic import BaseModel


class Student(BaseModel):
    id: str
    first_name: str
    last_name: str
    semester: int


class Registration(BaseModel):
    student_id: str
    course_id: str
    place: int
