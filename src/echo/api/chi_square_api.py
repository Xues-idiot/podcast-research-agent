"""卡方分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.chi_square import get_chi_square


router = APIRouter(prefix="/api/chi-square", tags=["chi-square"])


class ChiSquareRequest(BaseModel):
    x: float
    k: int


@router.post("/pdf")
async def pdf(request: ChiSquareRequest):
    return {"result": get_chi_square().pdf(request.x, request.k)}
