from pydantic import BaseModel


class Student(BaseModel):
    """
    Model studenta. Zawiera identyfikator, imię, nazwisko oraz jest przypisany do semestru.
    """
    id: str
    first_name: str
    last_name: str
    semester: int


class Registration(BaseModel):
    """
    Model rejestracji. Przechowuje identyfikatory studenta oraz kursu i miejsce studenta na liście.
    """
    student_id: str
    course_id: str
    place: int
