"""质数查找API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.prime_finder import get_prime_finder


router = APIRouter(prefix="/api/prime-finder", tags=["prime-finder"])


class PrimeFinderRequest(BaseModel):
    n: int


@router.post("/primes-up-to")
async def primes_up_to(request: PrimeFinderRequest):
    return {"result": get_prime_finder().primes_up_to(request.n)}
