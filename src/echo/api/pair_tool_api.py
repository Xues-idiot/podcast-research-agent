"""配对工具API"""

from fastapi import APIRouter

from echo.research.pair_tool import get_pair_tool


router = APIRouter(prefix="/api/pair", tags=["pair"])


@router.post("/make")
async def make_pair(first: str, second: str):
    return {"result": get_pair_tool().make_pair(first, second)}


@router.get("/first")
async def get_first(pair: list):
    return {"result": get_pair_tool().get_first(pair)}


@router.get("/second")
async def get_second(pair: list):
    return {"result": get_pair_tool().get_second(pair)}