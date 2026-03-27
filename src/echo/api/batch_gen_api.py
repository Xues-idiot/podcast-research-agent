"""范围生成API"""

from fastapi import APIRouter

from echo.research.batch_gen import get_range_generator


router = APIRouter(prefix="/api/batch", tags=["batch"])


@router.post("/range-int")
async def range_int(start: int, stop: int, step: int = 1):
    return {"result": get_range_generator().range_int(start, stop, step)}


@router.post("/range-float")
async def range_float(start: float, stop: float, step: float):
    return {"result": get_range_generator().range_float(start, stop, step)}