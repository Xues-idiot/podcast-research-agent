"""平均值API"""

from fastapi import APIRouter

from echo.research.averager import get_averager_tool


router = APIRouter(prefix="/api/averager", tags=["averager"])


@router.post("/mean")
async def mean(numbers: list):
    return {"result": get_averager_tool().mean(numbers)}


@router.post("/median")
async def median(numbers: list):
    return {"result": get_averager_tool().median(numbers)}


@router.post("/mode")
async def mode(numbers: list):
    return {"result": get_averager_tool().mode(numbers)}