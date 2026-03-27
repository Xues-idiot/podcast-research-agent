"""插入API"""

from fastapi import APIRouter

from echo.research.insert_tool import get_insert_tool


router = APIRouter(prefix="/api/insert", tags=["insert"])


@router.post("/insert")
async def insert(items: list, index: int, item):
    return {"result": get_insert_tool().insert(items, index, item)}