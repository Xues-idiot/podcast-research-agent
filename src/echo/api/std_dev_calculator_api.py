"""标准差计算器API"""

from fastapi import APIRouter

from echo.research.std_dev_calculator import get_std_dev_calculator


router = APIRouter(prefix="/api/std-dev-calc", tags=["std-dev-calc"])


@router.post("/stdev")
async def stdev(items: list):
    return {"result": get_std_dev_calculator().stdev(items)}
