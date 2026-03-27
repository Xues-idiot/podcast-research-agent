"""选择API"""

from fastapi import APIRouter

from echo.research.selector_tool import get_selector_tool


router = APIRouter(prefix="/api/selector", tags=["selector"])


@router.post("/first")
async def first(items: list):
    return {"result": get_selector_tool().first(items)}


@router.post("/last")
async def last(items: list):
    return {"result": get_selector_tool().last(items)}


@router.post("/nth")
async def nth(items: list, n: int):
    return {"result": get_selector_tool().nth(items, n)}