"""斐波那契API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.fibonacci_generator import get_fibonacci_generator


router = APIRouter(prefix="/api/fibonacci", tags=["fibonacci"])


class FibonacciRequest(BaseModel):
    n: int


@router.post("/fibonacci")
async def fibonacci(request: FibonacciRequest):
    return {"result": get_fibonacci_generator().fibonacci(request.n)}
