from src.registering.aggregates.course.aggregate import CourseRegistry
from src.registering.models import Student, Registration
from src.registering.repositories.course.base import CourseRepository
from src.registering.repositories.registry.base import RegistrationRepository
from src.registering.services.base import RegistrationService

from src.registering.aggregates.student.aggregate import StudentValidator


class RegistrationServiceV1(RegistrationService):
    def __init__(
        self, registration_repo: RegistrationRepository, course_repo: CourseRepository
    ) -> None:
        self.registration_repo = registration_repo
        self.course_repo = course_repo

    def get_registration(self, student_id: str, course_id: str) -> Registration:
        return self.registration_repo.get_registration(student_id, course_id)

    def register_student(self, course_id: str, student: Student) -> int:
        course_to_sign = self.course_repo.get_course(course_id)
        student_registrations = self.registration_repo.get_registrations(student.id)
        student_courses = self.course_repo.get_courses(
            [registration.course_id for registration in student_registrations]
        )
        StudentValidator(student, student_courses, course_to_sign).validate()
        result = CourseRegistry(course_to_sign).register(student)

        self.course_repo.update(result.course)
        self.registration_repo.insert(result.registration)
        return result.place
