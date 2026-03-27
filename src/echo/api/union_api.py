"""并集API"""

from fastapi import APIRouter

from echo.research.union_tool import get_union_tool


router = APIRouter(prefix="/api/union", tags=["union"])


@router.post("/union")
async def union(list1: list, list2: list):
    return {"result": get_union_tool().union(list1, list2)}