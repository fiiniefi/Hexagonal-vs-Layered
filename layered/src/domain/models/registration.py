from typing import List

from pydantic import BaseModel


class Student(BaseModel):
    id: str
    first_name: str
    last_name: str


class Registration(BaseModel):
    course_id: str
    registered_students: List[Student]
