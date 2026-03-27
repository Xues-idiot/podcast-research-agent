"""双二阶滤波API"""

from fastapi import APIRouter

from echo.research.biquad_filter import get_biquad_filter


router = APIRouter(prefix="/api/biquad", tags=["biquad"])


@router.post("/filter")
async def filter(data: list):
    return {"result": get_biquad_filter().filter(data)}
