"""基尼系数API"""

from fastapi import APIRouter

from echo.research.gini_coefficient import get_gini_coefficient


router = APIRouter(prefix="/api/gini", tags=["gini"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_gini_coefficient().gini(data)}
