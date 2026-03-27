"""交集API"""

from fastapi import APIRouter

from echo.research.intersect_tool import get_intersect_tool


router = APIRouter(prefix="/api/intersect", tags=["intersect"])


@router.post("/intersect")
async def intersect(list1: list, list2: list):
    return {"result": get_intersect_tool().intersect(list1, list2)}