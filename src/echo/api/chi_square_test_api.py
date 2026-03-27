"""卡方检验API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.chi_square_test import get_chi_square_test


router = APIRouter(prefix="/api/chi-square-test", tags=["chi-square-test"])


class ChiSquareTestRequest(BaseModel):
    observed: list
    expected: list


@router.post("/calculate")
async def calculate(request: ChiSquareTestRequest):
    return {"result": get_chi_square_test().chi_square(request.observed, request.expected)}
