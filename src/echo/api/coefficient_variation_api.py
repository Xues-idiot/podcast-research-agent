"""变异系数API"""

from fastapi import APIRouter

from echo.research.coefficient_variation import get_coefficient_variation


router = APIRouter(prefix="/api/cv", tags=["cv"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_coefficient_variation().cv(data)}
