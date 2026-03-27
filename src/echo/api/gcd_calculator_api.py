"""最大公约数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.gcd_calculator import get_gcd_calculator


router = APIRouter(prefix="/api/gcd-calc", tags=["gcd-calc"])


class GcdRequest(BaseModel):
    a: int
    b: int


@router.post("/gcd")
async def gcd(request: GcdRequest):
    return {"result": get_gcd_calculator().gcd(request.a, request.b)}
