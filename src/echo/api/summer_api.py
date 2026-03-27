"""求和API"""

from fastapi import APIRouter

from echo.research.summer import get_summer


router = APIRouter(prefix="/api/summer", tags=["summer"])


@router.post("/sum")
async def sum_values(items: list):
    return {"result": get_summer().sum(items)}