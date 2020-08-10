from src.registering.aggregates.course.registration import Registrator
from src.registering.models import Course, Student, RegistrationResponse


class CourseRegistry:
    def __init__(self, course: Course) -> None:
        self.registrator = Registrator(course)

    def register(self, student: Student) -> RegistrationResponse:
        return self.registrator.register(student)

    def withdraw(self) -> None:
        """
        A place where a registering is being withdrawn. All the students below should
        be moved upward
        """
        pass
