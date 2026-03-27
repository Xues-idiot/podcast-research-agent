"""追加API"""

from fastapi import APIRouter

from echo.research.append_tool import get_append_tool


router = APIRouter(prefix="/api/append", tags=["append"])


@router.post("/append")
async def append(items: list, item):
    return {"result": get_append_tool().append(items, item)}