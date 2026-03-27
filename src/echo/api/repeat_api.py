"""重复API"""

from fastapi import APIRouter

from echo.research.repeat_tool import get_repeat_tool


router = APIRouter(prefix="/api/repeat", tags=["repeat"])


@router.post("/repeat")
async def repeat(item, times: int):
    return {"result": get_repeat_tool().repeat(item, times)}