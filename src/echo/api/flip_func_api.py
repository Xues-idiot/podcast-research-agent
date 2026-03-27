"""翻转函数API"""

from fastapi import APIRouter

from echo.research.flip_func import get_flip_func


router = APIRouter(prefix="/api/flip", tags=["flip"])


@router.post("/flip")
async def flip():
    return {"result": None}
