"""查找API"""

from fastapi import APIRouter

from echo.research.find_tool import get_find_tool


router = APIRouter(prefix="/api/find", tags=["find"])


@router.post("/find")
async def find(items: list, predicate):
    return {"result": get_find_tool().find(items, predicate)}