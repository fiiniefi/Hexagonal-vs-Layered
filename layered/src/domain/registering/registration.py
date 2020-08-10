from dataclasses import dataclass

from src.domain.models.courses import Course
from src.domain.models.registration import Student, Registration
from src.infrastructure.courses.repository import MongoCoursesRepository
from src.infrastructure.registry.repository import MongoRegistrationRepository


@dataclass
class PlacesNumber:
    laboratories: int = 20
    seminar: int = 10


class Registrator:
    def __init__(self, course: Course) -> None:
        self.course = course
        self.registration_repo = MongoRegistrationRepository()
        self.course_repo = MongoCoursesRepository()

    def register(self, student: Student) -> int:
        self.course.student_ids.append(student.id)
        place = self._place_on_list()

        registration = Registration(
            student_id=student.id, course_id=self.course.id, place=place
        )
        self.registration_repo.insert(registration)
        self.course_repo.update(self.course)
        return place

    def _place_on_list(self) -> int:
        place = len(self.course.student_ids)
        number_of_places = getattr(PlacesNumber, self.course.type)
        course_overloaded = place > number_of_places
        return number_of_places - place if course_overloaded else place
