"""合并API"""

from fastapi import APIRouter

from echo.research.merge_tool import get_merge_tool


router = APIRouter(prefix="/api/merge", tags=["merge"])


@router.post("/merge")
async def merge(list1: list, list2: list):
    return {"result": get_merge_tool().merge(list1, list2)}