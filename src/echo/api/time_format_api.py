"""时间格式化API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.time_format import get_time_format_tool


router = APIRouter(prefix="/api/time-format", tags=["time-format"])


class DurationRequest(BaseModel):
    seconds: float


class TimestampRequest(BaseModel):
    ts: int


@router.post("/duration")
async def format_duration(request: DurationRequest):
    tool = get_time_format_tool()
    return {"result": tool.format_duration(request.seconds)}


@router.post("/timestamp")
async def format_timestamp(request: TimestampRequest):
    tool = get_time_format_tool()
    return {"result": tool.format_timestamp(request.ts)}


@router.post("/relative")
async def relative_time(request: TimestampRequest):
    tool = get_time_format_tool()
    return {"result": tool.relative_time(request.ts)}