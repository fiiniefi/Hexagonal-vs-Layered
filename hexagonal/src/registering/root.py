from src.conf.setup import mongo_db
from src.mailing.services.base import BaseMailingService
from src.mailing.services.fake import FakeMailingService
from src.registering.repositories.course.fake import FakeCourseRepository
from src.registering.repositories.course.mongo import MongoCourseRepository
from src.registering.repositories.registry.mongo import MongoRegistrationRepository
from src.registering.services.v1 import RegistrationServiceV1


"""
Composition root dla modułu registering. Abstrakcje ,,rozwiązują się'' na implementacje.
"""


def mongo_course_repository() -> MongoCourseRepository:
    return MongoCourseRepository(mongo_db())


def fake_course_repository() -> FakeCourseRepository:
    return FakeCourseRepository()


def mongo_registration_repository() -> MongoRegistrationRepository:
    return MongoRegistrationRepository(mongo_db())


def registration_service() -> RegistrationServiceV1:
    return RegistrationServiceV1(
        mongo_registration_repository(),
        mongo_course_repository(),
        fake_mailing_service(),
    )


def fake_mailing_service() -> BaseMailingService:
    return FakeMailingService()
