"""类型检测API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.type_detect import get_type_detect_tool


router = APIRouter(prefix="/api/type-detect", tags=["type-detect"])


@router.post("/detect")
async def detect(request: BaseModel):
    tool = get_type_detect_tool()
    return {"result": tool.detect(request.get("value"))}


@router.post("/is-primitive")
async def is_primitive(request: BaseModel):
    tool = get_type_detect_tool()
    return {"result": tool.is_primitive(request.get("value"))}


@router.post("/is-collection")
async def is_collection(request: BaseModel):
    tool = get_type_detect_tool()
    return {"result": tool.is_collection(request.get("value"))}


@router.post("/is-sequence")
async def is_sequence(request: BaseModel):
    tool = get_type_detect_tool()
    return {"result": tool.is_sequence(request.get("value"))}