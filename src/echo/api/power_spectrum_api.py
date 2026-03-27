"""功率谱API"""

from fastapi import APIRouter

from echo.research.power_spectrum import get_power_spectrum


router = APIRouter(prefix="/api/power-spectrum", tags=["power-spectrum"])


@router.post("/compute")
async def compute(signal: list):
    return {"result": get_power_spectrum().compute(signal)}
