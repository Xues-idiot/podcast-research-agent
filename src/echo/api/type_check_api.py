"""类型检测API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.type_check import get_type_check_tool


router = APIRouter(prefix="/api/type-check", tags=["type-check"])


class CheckRequest(BaseModel):
    value: Any


@router.post("/get-type")
async def get_type(request: CheckRequest):
    tool = get_type_check_tool()
    return {"type": tool.get_type(request.value)}


@router.post("/is-string")
async def is_string(request: CheckRequest):
    tool = get_type_check_tool()
    return {"result": tool.is_string(request.value)}


@router.post("/is-number")
async def is_number(request: CheckRequest):
    tool = get_type_check_tool()
    return {"result": tool.is_number(request.value)}


@router.post("/is-bool")
async def is_bool(request: CheckRequest):
    tool = get_type_check_tool()
    return {"result": tool.is_bool(request.value)}


@router.post("/is-list")
async def is_list(request: CheckRequest):
    tool = get_type_check_tool()
    return {"result": tool.is_list(request.value)}


@router.post("/is-dict")
async def is_dict(request: CheckRequest):
    tool = get_type_check_tool()
    return {"result": tool.is_dict(request.value)}