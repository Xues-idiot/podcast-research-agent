"""切片API"""

from fastapi import APIRouter

from echo.research.slicer_tool import get_slicer_tool


router = APIRouter(prefix="/api/slicer", tags=["slicer"])


@router.post("/slice")
async def slice_items(items: list, start: int, end: int = None):
    return {"result": get_slicer_tool().slice(items, start, end)}