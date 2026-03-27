"""切片API"""

from fastapi import APIRouter

from echo.research.slice_tool import get_slice_tool


router = APIRouter(prefix="/api/slice", tags=["slice"])


@router.post("/slice")
async def slice(items: list, start: int = 0, end: int = None):
    return {"result": get_slice_tool().slice(items, start, end)}