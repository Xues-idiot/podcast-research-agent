"""阶乘API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.factorial_calculator import get_factorial_calculator


router = APIRouter(prefix="/api/factorial-calc", tags=["factorial-calc"])


class FactorialRequest(BaseModel):
    n: int


@router.post("/factorial")
async def factorial(request: FactorialRequest):
    return {"result": get_factorial_calculator().factorial(request.n)}
