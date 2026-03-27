"""空值检查API"""

from fastapi import APIRouter

from echo.research.null_checker import get_null_checker_tool


router = APIRouter(prefix="/api/null-checker", tags=["null-checker"])


@router.post("/is-none")
async def is_none(value):
    return {"result": get_null_checker_tool().is_none(value)}


@router.post("/is-empty")
async def is_empty(value):
    return {"result": get_null_checker_tool().is_empty(value)}


@router.post("/is-none-or-empty")
async def is_none_or_empty(value):
    return {"result": get_null_checker_tool().is_none_or_empty(value)}