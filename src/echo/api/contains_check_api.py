"""包含检查API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.contains_check import get_contains_check_tool


router = APIRouter(prefix="/api/contains-check", tags=["contains-check"])


class CheckRequest(BaseModel):
    text: str
    value: str


@router.post("/contains")
async def contains(request: CheckRequest):
    tool = get_contains_check_tool()
    return {"result": tool.contains(request.text, request.value)}


@router.post("/starts-with")
async def starts_with(request: CheckRequest):
    tool = get_contains_check_tool()
    return {"result": tool.starts_with(request.text, request.value)}


@router.post("/ends-with")
async def ends_with(request: CheckRequest):
    tool = get_contains_check_tool()
    return {"result": tool.ends_with(request.text, request.value)}