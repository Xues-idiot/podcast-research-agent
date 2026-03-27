"""索引查找API"""

from fastapi import APIRouter

from echo.research.index_of_tool import get_index_of_tool


router = APIRouter(prefix="/api/index-of", tags=["index-of"])


@router.post("/index-of")
async def index_of(items: list, item):
    return {"result": get_index_of_tool().index_of(items, item)}