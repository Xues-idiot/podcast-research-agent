"""日期计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.date_calc import get_date_calc_tool


router = APIRouter(prefix="/api/date-calc", tags=["date-calc"])


class AddDaysRequest(BaseModel):
    date_str: str
    days: int


class DaysBetweenRequest(BaseModel):
    date1: str
    date2: str


class WeekendRequest(BaseModel):
    date_str: str


@router.post("/add-days")
async def add_days(request: AddDaysRequest):
    tool = get_date_calc_tool()
    return {"result": tool.add_days(request.date_str, request.days)}


@router.post("/days-between")
async def days_between(request: DaysBetweenRequest):
    tool = get_date_calc_tool()
    return {"result": tool.days_between(request.date1, request.date2)}


@router.post("/is-weekend")
async def is_weekend(request: WeekendRequest):
    tool = get_date_calc_tool()
    return {"result": tool.is_weekend(request.date_str)}