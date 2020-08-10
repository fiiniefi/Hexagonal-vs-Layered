from datetime import datetime
from typing import List

from pydantic import BaseModel


class Course(BaseModel):
    id: str
    name: str
    semester: int
    student_ids: List[str]
    date_time: datetime
    type: str
