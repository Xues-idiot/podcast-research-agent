"""格式化工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.format_utils import format_json, format_number, format_currency, format_percent, format_file_size, format_duration, format_phone, format_list


class JsonRequest(BaseModel):
    obj: Any
    indent: int = 2


class NumberRequest(BaseModel):
    num: float
    decimals: int = 2


class CurrencyRequest(BaseModel):
    amount: float
    symbol: str = "¥"


class PercentRequest(BaseModel):
    value: float
    decimals: int = 1


class FileSizeRequest(BaseModel):
    bytes: int


class DurationRequest(BaseModel):
    seconds: int


class PhoneRequest(BaseModel):
    phone: str


class ListRequest(BaseModel):
    items: List
    separator: str = ", "
    last_separator: str = " 和 "


router = APIRouter(prefix="/api/format", tags=["format"])


@router.post("/json")
async def json_fmt(request: JsonRequest) -> dict:
    return {"result": format_json(request.obj, request.indent)}


@router.post("/number")
async def number_fmt(request: NumberRequest) -> dict:
    return {"result": format_number(request.num, request.decimals)}


@router.post("/currency")
async def currency_fmt(request: CurrencyRequest) -> dict:
    return {"result": format_currency(request.amount, request.symbol)}


@router.post("/percent")
async def percent_fmt(request: PercentRequest) -> dict:
    return {"result": format_percent(request.value, request.decimals)}


@router.post("/file-size")
async def file_size_fmt(request: FileSizeRequest) -> dict:
    return {"result": format_file_size(request.bytes)}


@router.post("/duration")
async def duration_fmt(request: DurationRequest) -> dict:
    return {"result": format_duration(request.seconds)}


@router.post("/phone")
async def phone_fmt(request: PhoneRequest) -> dict:
    return {"result": format_phone(request.phone)}


@router.post("/list")
async def list_fmt(request: ListRequest) -> dict:
    return {"result": format_list(request.items, request.separator, request.last_separator)}
