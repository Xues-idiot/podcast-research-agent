"""格式化输出API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, List

from echo.research.format_pretty import get_format_pretty_tool


router = APIRouter(prefix="/api/format-pretty", tags=["format-pretty"])


class PrettyJsonRequest(BaseModel):
    data: Any
    indent: int = 2


@router.post("/json")
async def pretty_json(request: PrettyJsonRequest):
    tool = get_format_pretty_tool()
    return {"result": tool.pretty_json(request.data, request.indent)}


class PrettyListRequest(BaseModel):
    items: List[Any]
    bullet: str = "- "


@router.post("/list")
async def pretty_list(request: PrettyListRequest):
    tool = get_format_pretty_tool()
    return {"result": tool.pretty_list(request.items, request.bullet)}


class PrettyDictRequest(BaseModel):
    data: dict
    indent: int = 2


@router.post("/dict")
async def pretty_dict(request: PrettyDictRequest):
    tool = get_format_pretty_tool()
    return {"result": tool.pretty_dict(request.data, request.indent)}


class TableRequest(BaseModel):
    headers: List[str]
    rows: List[List[Any]]


@router.post("/table")
async def table_format(request: TableRequest):
    tool = get_format_pretty_tool()
    return {"result": tool.table_format(request.headers, request.rows)}


class TruncateRequest(BaseModel):
    text: str
    max_len: int = 50


@router.post("/truncate")
async def truncate_middle(request: TruncateRequest):
    tool = get_format_pretty_tool()
    return {"result": tool.truncate_middle(request.text, request.max_len)}