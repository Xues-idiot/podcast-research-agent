"""四分位距API"""

from fastapi import APIRouter

from echo.research.interquartile_range import get_interquartile_range


router = APIRouter(prefix="/api/iqr", tags=["iqr"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_interquartile_range().iqr(data)}
