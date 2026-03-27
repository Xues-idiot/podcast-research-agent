"""差异API"""

from fastapi import APIRouter

from echo.research.diff_tool import get_diff_tool


router = APIRouter(prefix="/api/diff", tags=["diff"])


@router.post("/diff")
async def diff(list1: list, list2: list):
    return {"result": get_diff_tool().diff(list1, list2)}