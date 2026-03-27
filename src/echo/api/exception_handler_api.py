"""异常处理API"""

from fastapi import APIRouter

from echo.research.exception_handler import get_exception_handler


router = APIRouter(prefix="/api/exception-handler", tags=["exception-handler"])


@router.post("/handle")
async def handle(func, handler):
    return {"result": get_exception_handler().handle(func, handler)}