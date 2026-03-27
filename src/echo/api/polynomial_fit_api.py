"""多项式拟合API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.polynomial_fit import get_polynomial_fit


router = APIRouter(prefix="/api/polynomial-fit", tags=["polynomial-fit"])


class PolyRequest(BaseModel):
    x: list
    y: list


@router.post("/fit-linear")
async def fit_linear(request: PolyRequest):
    return {"result": get_polynomial_fit().fit_linear(request.x, request.y)}
