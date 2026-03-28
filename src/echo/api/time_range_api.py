"""时间范围API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

from echo.research.time_range import get_time_range_tool


router = APIRouter(prefix="/api/time-range", tags=["time-range"])


class RangeRequest(BaseModel):
    start: str
    end: str
    step_minutes: int = 60


@router.post("/create-range")
async def create_range(request: RangeRequest):
    tool = get_time_range_tool()
    start_dt = datetime.fromisoformat(request.start)
    end_dt = datetime.fromisoformat(request.end)
    result = tool.create_range(start_dt, end_dt, request.step_minutes)
    return {"range": [r.isoformat() for r in result]}


class WithinRangeRequest(BaseModel):
    dt: str
    start: str
    end: str


@router.post("/within-range")
async def within_range(request: WithinRangeRequest):
    tool = get_time_range_tool()
    dt = datetime.fromisoformat(request.dt)
    start = datetime.fromisoformat(request.start)
    end = datetime.fromisoformat(request.end)
    return {"within": tool.is_within_range(dt, start, end)}


class OverlapRequest(BaseModel):
    start1: str
    end1: str
    start2: str
    end2: str


@router.post("/overlap")
async def overlap(request: OverlapRequest):
    tool = get_time_range_tool()
    start1 = datetime.fromisoformat(request.start1)
    end1 = datetime.fromisoformat(request.end1)
    start2 = datetime.fromisoformat(request.start2)
    end2 = datetime.fromisoformat(request.end2)
    result = tool.get_overlap(start1, end1, start2, end2)
    if result:
        return {"overlap": {"start": result[0].isoformat(), "end": result[1].isoformat()}}
    return {"overlap": None}