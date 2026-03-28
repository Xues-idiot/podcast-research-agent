"""格式转换API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any

from echo.research.format_convert import get_format_convert_tool


router = APIRouter(prefix="/api/format-convert", tags=["format-convert"])


class DictToListRequest(BaseModel):
    data: Dict[str, Any]
    separator: str = "|"


@router.post("/dict-to-list")
async def dict_to_list(request: DictToListRequest):
    tool = get_format_convert_tool()
    return {"result": tool.dict_to_list(request.data, request.separator)}


class ListToDictRequest(BaseModel):
    items: List[str]
    separator: str = "|"


@router.post("/list-to-dict")
async def list_to_dict(request: ListToDictRequest):
    tool = get_format_convert_tool()
    return {"result": tool.list_to_dict(request.items, request.separator)}


class FlattenDictRequest(BaseModel):
    data: Dict[str, Any]
    separator: str = "."


@router.post("/flatten-dict")
async def flatten_dict(request: FlattenDictRequest):
    tool = get_format_convert_tool()
    return {"result": tool.flatten_dict(request.data, sep=request.separator)}


class UnflattenDictRequest(BaseModel):
    data: Dict[str, Any]
    separator: str = "."


@router.post("/unflatten-dict")
async def unflatten_dict(request: UnflattenDictRequest):
    tool = get_format_convert_tool()
    return {"result": tool.unflatten_dict(request.data, sep=request.separator)}


class ListToStringRequest(BaseModel):
    items: List[Any]
    separator: str = ", "


@router.post("/list-to-string")
async def list_to_string(request: ListToStringRequest):
    tool = get_format_convert_tool()
    return {"result": tool.list_to_string(request.items, request.separator)}


class StringToListRequest(BaseModel):
    text: str
    separator: str = ", "


@router.post("/string-to-list")
async def string_to_list(request: StringToListRequest):
    tool = get_format_convert_tool()
    return {"result": tool.string_to_list(request.text, request.separator)}