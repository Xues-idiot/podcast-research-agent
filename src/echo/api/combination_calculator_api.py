"""组合API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.combination_calculator import get_combination_calculator


router = APIRouter(prefix="/api/combination-calc", tags=["combination-calc"])


class CombinationRequest(BaseModel):
    n: int
    r: int


@router.post("/combinations")
async def combinations(request: CombinationRequest):
    return {"result": get_combination_calculator().combinations(request.n, request.r)}
