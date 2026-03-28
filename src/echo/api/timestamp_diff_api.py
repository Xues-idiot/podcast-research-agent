"""时间戳差计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.timestamp_diff import get_timestamp_diff_tool


router = APIRouter(prefix="/api/timestamp-diff", tags=["timestamp-diff"])


class DiffRequest(BaseModel):
    ts1: int
    ts2: int


@router.post("/seconds")
async def seconds_between(request: DiffRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.seconds_between(request.ts1, request.ts2)}


@router.post("/minutes")
async def minutes_between(request: DiffRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.minutes_between(request.ts1, request.ts2)}


@router.post("/hours")
async def hours_between(request: DiffRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.hours_between(request.ts1, request.ts2)}


@router.post("/days")
async def days_between(request: DiffRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.days_between(request.ts1, request.ts2)}


class WithinSecondsRequest(BaseModel):
    ts1: int
    ts2: int
    threshold: int


@router.post("/within-seconds")
async def is_within_seconds(request: WithinSecondsRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.is_within_seconds(request.ts1, request.ts2, request.threshold)}


class AgeRequest(BaseModel):
    timestamp: int


@router.post("/age")
async def age(request: AgeRequest):
    tool = get_timestamp_diff_tool()
    return {"result": tool.age_string(request.timestamp)}