from src.domain.models.registration import Registration, Student
from src.domain.registering.registration import Registrator
from src.domain.registering.validator import StudentValidator
from src.infrastructure.courses.repository import MongoCoursesRepository
from src.infrastructure.registry.repository import MongoRegistrationRepository


class RegistrationService:
    def __init__(self) -> None:
        self.registration_repo = MongoRegistrationRepository()
        self.courses_repo = MongoCoursesRepository()

    def get_registration(self, course_id: str) -> Registration:
        return self.registration_repo.get_registration(course_id)

    def register_student(self, course_id: str, student: Student) -> int:
        courses_repo = MongoCoursesRepository()
        courses = courses_repo.get_courses()
        student_courses = [
            course for course in courses if student.id in course.student_ids
        ]
        course_to_sign = self.courses_repo.get_course(course_id)
        StudentValidator(student, student_courses, course_to_sign).validate()
        return Registrator(course_to_sign).register(student)
