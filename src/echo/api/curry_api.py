"""柯里化API"""

from fastapi import APIRouter

from echo.research.curry_tool import get_curry_tool


router = APIRouter(prefix="/api/curry", tags=["curry"])


@router.post("/curry")
async def curry(func):
    return {"result": get_curry_tool().curry(func)}