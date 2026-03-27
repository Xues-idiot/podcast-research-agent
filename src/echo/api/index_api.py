"""索引API"""

from fastapi import APIRouter

from echo.research.index_tool import get_index_tool


router = APIRouter(prefix="/api/index", tags=["index"])


@router.post("/index")
async def index(items: list, item):
    return {"result": get_index_tool().index(items, item)}