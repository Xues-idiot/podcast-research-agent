"""卡尔曼平滑API"""

from fastapi import APIRouter

from echo.research.kalman_smoother import get_kalman_smoother


router = APIRouter(prefix="/api/kalman-smoother", tags=["kalman-smoother"])


@router.post("/smooth")
async def smooth(measurements: list):
    return {"result": get_kalman_smoother().smooth(measurements)}
