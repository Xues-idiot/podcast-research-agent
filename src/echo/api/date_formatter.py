"""日期格式化API"""

from fastapi import APIRouter
from datetime import datetime

from echo.research.date_formatter import get_date_formatter


router = APIRouter(prefix="/api/date", tags=["date"])


@router.post("/format")
async def format_date(dt: str, format_str: str = "%Y-%m-%d %H:%M:%S"):
    parsed = get_date_formatter().parse_datetime(dt)
    return {"result": get_date_formatter().format_datetime(parsed, format_str)}


@router.get("/now")
async def now(format_str: str = "%Y-%m-%d %H:%M:%S"):
    return {"result": get_date_formatter().now(format_str)}


@router.post("/to_iso")
async def to_iso(dt: str):
    parsed = get_date_formatter().parse_datetime(dt)
    return {"result": get_date_formatter().to_iso(parsed)}