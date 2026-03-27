"""累加器API"""

from fastapi import APIRouter

from echo.research.accumulator import get_accumulator_tool


router = APIRouter(prefix="/api/accumulator", tags=["accumulator"])


@router.post("/accumulate")
async def accumulate(items: list):
    return {"result": get_accumulator_tool().accumulate(items)}


@router.post("/running-sum")
async def running_sum(items: list):
    return {"result": get_accumulator_tool().running_sum(items)}