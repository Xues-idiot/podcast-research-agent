"""质数API"""

from fastapi import APIRouter

from echo.research.prime_numbers import get_prime_tool


router = APIRouter(prefix="/api/prime", tags=["prime"])


@router.post("/is_prime")
async def is_prime(n: int):
    return {"result": get_prime_tool().is_prime(n)}


@router.post("/primes_up_to")
async def primes_up_to(n: int):
    return {"primes": get_prime_tool().primes_up_to(n)}