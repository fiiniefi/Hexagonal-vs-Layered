from dataclasses import dataclass

from src.registering.models import Student, Course, Registration, RegistrationResponse


@dataclass
class PlacesNumber:
    laboratories: int = 20
    seminar: int = 10


class Registrator:
    def __init__(self, course: Course) -> None:
        self.course = course

    def register(self, student: Student) -> RegistrationResponse:
        self.course.student_ids.append(student.id)
        place = self._place_on_list()

        registration = Registration(
            student_id=student.id, course_id=self.course.id, place=place
        )
        return RegistrationResponse(
            course=self.course, registration=registration, place=place
        )

    def _place_on_list(self) -> int:
        place = len(self.course.student_ids)
        number_of_places = getattr(PlacesNumber, self.course.type)
        course_overloaded = place > number_of_places
        return number_of_places - place if course_overloaded else place
