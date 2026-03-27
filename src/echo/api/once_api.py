"""单次执行API"""

from fastapi import APIRouter

from echo.research.once_tool import get_once_tool


router = APIRouter(prefix="/api/once", tags=["once"])


@router.post("/once")
async def once(func):
    return {"result": get_once_tool().once(func)}