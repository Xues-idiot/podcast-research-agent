"""数字格式化API"""

from fastapi import APIRouter

from echo.research.number_formatter import get_number_formatter


router = APIRouter(prefix="/api/number", tags=["number"])


@router.post("/currency")
async def format_currency(amount: float, currency: str = "CNY"):
    return {"result": get_number_formatter().format_currency(amount, currency)}


@router.post("/percentage")
async def format_percentage(value: float, decimals: int = 2):
    return {"result": get_number_formatter().format_percentage(value, decimals)}


@router.post("/bytes")
async def format_bytes(bytes_count: int):
    return {"result": get_number_formatter().format_bytes(bytes_count)}