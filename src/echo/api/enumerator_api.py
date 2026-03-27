"""枚举API"""

from fastapi import APIRouter

from echo.research.enumerator_tool import get_enumerator_tool


router = APIRouter(prefix="/api/enumerator", tags=["enumerator"])


@router.post("/enumerate")
async def enumerate_items(items: list, start: int = 0):
    return {"result": get_enumerator_tool().enumerate_items(items, start)}