"""绑定API"""

from fastapi import APIRouter

from echo.research.binding import get_binding_tool


router = APIRouter(prefix="/api/binding", tags=["binding"])


@router.post("/bind-first")
async def bind_first(func, first_arg):
    return {"result": get_binding_tool().bind_first(func, first_arg)}


@router.post("/bind-last")
async def bind_last(func, last_arg):
    return {"result": get_binding_tool().bind_last(func, last_arg)}