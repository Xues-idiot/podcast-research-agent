"""参数翻转API"""

from fastapi import APIRouter

from echo.research.flip_tool import get_flip_tool


router = APIRouter(prefix="/api/flip", tags=["flip"])


@router.post("/flip")
async def flip(func):
    return {"result": get_flip_tool().flip(func)}