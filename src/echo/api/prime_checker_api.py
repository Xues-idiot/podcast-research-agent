"""质数检查API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.prime_checker import get_prime_checker


router = APIRouter(prefix="/api/prime-checker", tags=["prime-checker"])


class PrimeRequest(BaseModel):
    n: int


@router.post("/is-prime")
async def is_prime(request: PrimeRequest):
    return {"result": get_prime_checker().is_prime(request.n)}
