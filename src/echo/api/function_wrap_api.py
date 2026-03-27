"""函数包装API"""

from fastapi import APIRouter

from echo.research.function_wrap import get_function_wrapper


router = APIRouter(prefix="/api/function-wrap", tags=["function-wrap"])


@router.post("/wrap")
async def wrap(func):
    return {"result": get_function_wrapper().wrap(func)}


@router.post("/before")
async def before(func, before_func):
    return {"result": get_function_wrapper().before(func, before_func)}


@router.post("/after")
async def after(func, after_func):
    return {"result": get_function_wrapper().after(func, after_func)}