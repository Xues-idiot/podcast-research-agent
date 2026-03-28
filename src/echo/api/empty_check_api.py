"""空值检查API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any

from echo.research.empty_check import get_empty_check_tool


router = APIRouter(prefix="/api/empty-check", tags=["empty-check"])


class CheckRequest(BaseModel):
    value: Any


@router.post("/is-empty")
async def is_empty(request: CheckRequest):
    tool = get_empty_check_tool()
    return {"result": tool.is_empty(request.value)}


@router.post("/is-not-empty")
async def is_not_empty(request: CheckRequest):
    tool = get_empty_check_tool()
    return {"result": tool.is_not_empty(request.value)}