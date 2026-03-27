"""卡尔曼滤波API"""

from fastapi import APIRouter

from echo.research.kalman_filter import get_kalman_filter


router = APIRouter(prefix="/api/kalman", tags=["kalman"])


@router.post("/filter")
async def filter(measurements: list):
    return {"result": get_kalman_filter().filter(measurements)}
