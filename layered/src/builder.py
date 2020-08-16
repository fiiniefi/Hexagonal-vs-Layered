from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from requests import Request
from starlette.responses import JSONResponse

from src.domain.exceptions import InvalidRegistration
from src.exceptions import NotFound
from src.presentation.courses.endpoints import router as courses_router
from src.presentation.registering.endpoints import router as registration_router


"""
Budowa aplikacji. W kontekście porównania architektur nie zawiera walorów dydaktycznych, 
więc komentowanie tej części jest pominęte.
"""


class APIBuilder:
    def __init__(self) -> None:
        self.app = FastAPI()

    def build(self) -> FastAPI:
        self.app.include_router(courses_router, prefix="/courses", tags=["courses"])
        self.app.include_router(
            registration_router, prefix="/registry", tags=["registry"]
        )
        self.app.add_exception_handler(
            InvalidRegistration, invalid_registration_exception_handler
        )
        self.app.add_exception_handler(NotFound, not_found_exception_handler)
        return self.app


async def invalid_registration_exception_handler(
    request: Request, error_type: InvalidRegistration
) -> JSONResponse:
    return await http_exception_handler(
        request, HTTPException(400, detail=str(error_type))
    )


async def not_found_exception_handler(
    request: Request,
    error_type: NotFound,
) -> JSONResponse:
    return await http_exception_handler(
        request, HTTPException(400, detail=str(error_type))
    )
