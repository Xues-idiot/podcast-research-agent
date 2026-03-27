"""对数API"""

from fastapi import APIRouter

from echo.research.log_tool import get_log_tool


router = APIRouter(prefix="/api/log", tags=["log"])


@router.post("/log")
async def log(value: float, base: float = None):
    if base:
        return {"result": get_log_tool().log(value, base)}
    return {"result": get_log_tool().log(value)}


@router.post("/log10")
async def log10(value: float):
    return {"result": get_log_tool().log10(value)}


@router.post("/log2")
async def log2(value: float):
    return {"result": get_log_tool().log2(value)}