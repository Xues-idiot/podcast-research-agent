"""平滑工具API"""

from fastapi import APIRouter

from echo.research.smoothing_tool import get_smoothing_tool


router = APIRouter(prefix="/api/smoothing", tags=["smoothing"])


@router.post("/moving-average")
async def moving_average(data: list[float], window: int = 3):
    tool = get_smoothing_tool()
    return {"result": tool.moving_average(data, window)}
