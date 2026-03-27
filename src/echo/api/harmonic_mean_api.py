"""调和平均API"""

from fastapi import APIRouter

from echo.research.harmonic_mean import get_harmonic_mean


router = APIRouter(prefix="/api/harmonic-mean", tags=["harmonic-mean"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_harmonic_mean().harmonic_mean(data)}
