"""类型转换API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.type_convert import get_type_convert_tool


router = APIRouter(prefix="/api/type-convert", tags=["type-convert"])


class ConvertRequest(BaseModel):
    value: Any


@router.post("/to-int")
async def to_int(request: ConvertRequest):
    tool = get_type_convert_tool()
    return {"result": tool.to_int(request.value)}


@router.post("/to-float")
async def to_float(request: ConvertRequest):
    tool = get_type_convert_tool()
    return {"result": tool.to_float(request.value)}


@router.post("/to-str")
async def to_str(request: ConvertRequest):
    tool = get_type_convert_tool()
    return {"result": tool.to_str(request.value)}


@router.post("/to-bool")
async def to_bool(request: ConvertRequest):
    tool = get_type_convert_tool()
    return {"result": tool.to_bool(request.value)}