"""序列生成API"""

from fastapi import APIRouter

from echo.research.sequence_gen import get_sequence_gen


router = APIRouter(prefix="/api/sequence", tags=["sequence"])


@router.post("/arithmetic")
async def arithmetic(start: float, step: float, count: int):
    return {"result": get_sequence_gen().arithmetic(start, step, count)}


@router.post("/geometric")
async def geometric(start: float, ratio: float, count: int):
    return {"result": get_sequence_gen().geometric(start, ratio, count)}


@router.post("/fibonacci")
async def fibonacci(count: int):
    return {"result": get_sequence_gen().fibonacci(count)}