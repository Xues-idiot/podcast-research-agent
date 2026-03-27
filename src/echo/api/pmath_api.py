"""幂API"""

from fastapi import APIRouter

from echo.research.pmath import get_power_tool


router = APIRouter(prefix="/api/power", tags=["power"])


@router.post("/power")
async def power(base: float, exponent: float):
    return {"result": get_power_tool().power(base, exponent)}


@router.post("/square")
async def square(value: float):
    return {"result": get_power_tool().square(value)}


@router.post("/cube")
async def cube(value: float):
    return {"result": get_power_tool().cube(value)}


@router.post("/sqrt")
async def sqrt(value: float):
    return {"result": get_power_tool().sqrt(value)}