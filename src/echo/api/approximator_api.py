"""近似API"""

from fastapi import APIRouter

from echo.research.approximator import get_approximator_tool


router = APIRouter(prefix="/api/approximator", tags=["approximator"])


@router.post("/round-to")
async def round_to(value: float, precision: int):
    return {"result": get_approximator_tool().round_to(value, precision)}


@router.post("/floor-to")
async def floor_to(value: float, precision: int):
    return {"result": get_approximator_tool().floor_to(value, precision)}


@router.post("/ceil-to")
async def ceil_to(value: float, precision: int):
    return {"result": get_approximator_tool().ceil_to(value, precision)}