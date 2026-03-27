"""熵API"""

from fastapi import APIRouter

from echo.research.entropy_calculator import get_entropy_calculator


router = APIRouter(prefix="/api/entropy", tags=["entropy"])


@router.post("/calculate")
async def calculate(data: list):
    return {"result": get_entropy_calculator().entropy(data)}
