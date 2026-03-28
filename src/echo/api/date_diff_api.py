"""日期差计算API"""

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, date

from echo.research.date_diff import get_date_diff_tool


router = APIRouter(prefix="/api/date-diff", tags=["date-diff"])


class DaysRequest(BaseModel):
    start: str
    end: str


@router.post("/days-between")
async def days_between(request: DaysRequest):
    tool = get_date_diff_tool()
    start = date.fromisoformat(request.start)
    end = date.fromisoformat(request.end)
    return {"days": tool.days_between(start, end)}


class HoursRequest(BaseModel):
    start: str
    end: str


@router.post("/hours-between")
async def hours_between(request: HoursRequest):
    tool = get_date_diff_tool()
    start = datetime.fromisoformat(request.start)
    end = datetime.fromisoformat(request.end)
    return {"hours": tool.hours_between(start, end)}


class MinutesRequest(BaseModel):
    start: str
    end: str


@router.post("/minutes-between")
async def minutes_between(request: MinutesRequest):
    tool = get_date_diff_tool()
    start = datetime.fromisoformat(request.start)
    end = datetime.fromisoformat(request.end)
    return {"minutes": tool.minutes_between(start, end)}


class AddDaysRequest(BaseModel):
    dt: str
    days: int


@router.post("/add-days")
async def add_days(request: AddDaysRequest):
    tool = get_date_diff_tool()
    dt = date.fromisoformat(request.dt)
    return {"result": tool.add_days(dt, request.days).isoformat()}


class AddMonthsRequest(BaseModel):
    dt: str
    months: int


@router.post("/add-months")
async def add_months(request: AddMonthsRequest):
    tool = get_date_diff_tool()
    dt = date.fromisoformat(request.dt)
    return {"result": tool.add_months(dt, request.months).isoformat()}