"""随机数API"""

from fastapi import APIRouter

from echo.research.random_tool import get_random_tool


router = APIRouter(prefix="/api/random", tags=["random"])


@router.post("/int")
async def random_int(low: int, high: int):
    return {"result": get_random_tool().random_int(low, high)}


@router.post("/float")
async def random_float():
    return {"result": get_random_tool().random_float()}


@router.post("/choice")
async def random_choice(items: list):
    return {"result": get_random_tool().random_choice(items)}


@router.post("/shuffle")
async def shuffle(items: list):
    return {"result": get_random_tool().shuffle(items)}