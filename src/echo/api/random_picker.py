"""随机选择API"""

from fastapi import APIRouter

from echo.research.random_picker import get_random_picker


router = APIRouter(prefix="/api/random", tags=["random"])


@router.post("/pick_one")
async def pick_one(items: list):
    return {"result": get_random_picker().pick_one(items)}


@router.post("/pick_multiple")
async def pick_multiple(items: list, count: int):
    return {"result": get_random_picker().pick_multiple(items, count)}


@router.post("/shuffle")
async def shuffle(items: list):
    return {"result": get_random_picker().shuffle(items)}