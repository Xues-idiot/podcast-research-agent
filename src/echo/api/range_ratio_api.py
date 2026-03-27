"""极差比API"""

from fastapi import APIRouter

from echo.research.range_ratio import get_range_ratio


router = APIRouter(prefix="/api/range-ratio", tags=["range-ratio"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_range_ratio().range_ratio(data)}
