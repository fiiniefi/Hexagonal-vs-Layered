from fastapi import FastAPI

from src.registration.api.endpoints import router as registration_router
from src.courses.api.endpoints import router as courses_router


class APIBuilder:
    def __init__(self) -> None:
        self.app = FastAPI()

    def build(self) -> FastAPI:
        self.app.include_router(courses_router, prefix="/courses", tags=["courses"])
        self.app.include_router(
            registration_router, prefix="/registry", tags=["registry"]
        )
        return self.app
