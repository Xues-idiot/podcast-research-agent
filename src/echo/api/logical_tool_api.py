"""逻辑工具API"""

from fastapi import APIRouter

from echo.research.logical_tool import get_logical_tool


router = APIRouter(prefix="/api/logical", tags=["logical"])


@router.post("/and")
async def and_(*args):
    return {"result": get_logical_tool().and_(*args)}


@router.post("/or")
async def or_(*args):
    return {"result": get_logical_tool().or_(*args)}


@router.post("/not")
async def not_(value):
    return {"result": get_logical_tool().not_(value)}