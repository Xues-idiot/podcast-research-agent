"""深拷贝API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.copy_deep import get_copy_deep_tool


router = APIRouter(prefix="/api/copy-deep", tags=["copy-deep"])


@router.post("/deep-copy")
async def deep_copy(request: BaseModel):
    tool = get_copy_deep_tool()
    return {"result": tool.deep_copy(request.get("obj"))}


@router.post("/shallow-copy")
async def shallow_copy(request: BaseModel):
    tool = get_copy_deep_tool()
    return {"result": tool.shallow_copy(request.get("obj"))}