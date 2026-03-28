"""数字格式化API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.number_fmt import get_number_fmt_tool


router = APIRouter(prefix="/api/number-fmt", tags=["number-fmt"])


class CurrencyRequest(BaseModel):
    value: float
    currency: str = "CNY"


@router.post("/currency")
async def format_currency(request: CurrencyRequest):
    tool = get_number_fmt_tool()
    return {"result": tool.format_currency(request.value, request.currency)}


class PercentRequest(BaseModel):
    value: float
    decimals: int = 2


@router.post("/percent")
async def format_percent(request: PercentRequest):
    tool = get_number_fmt_tool()
    return {"result": tool.format_percent(request.value, request.decimals)}


@router.post("/scientific")
async def format_scientific(request: BaseModel):
    tool = get_number_fmt_tool()
    return {"result": tool.format_scientific(request.get("value", 0))}


@router.post("/compact")
async def format_compact(request: BaseModel):
    tool = get_number_fmt_tool()
    return {"result": tool.format_compact(request.get("value", 0))}


class CommasRequest(BaseModel):
    value: float
    decimals: int = 0


@router.post("/with-commas")
async def format_with_commas(request: CommasRequest):
    tool = get_number_fmt_tool()
    return {"result": tool.format_with_commas(request.value, request.decimals)}


class OrdinalRequest(BaseModel):
    n: int


@router.post("/ordinal")
async def ordinal(request: OrdinalRequest):
    tool = get_number_fmt_tool()
    return {"result": tool.ordinal(request.n)}