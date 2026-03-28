"""星期计算API"""

from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date

from echo.research.weekday_calc import get_weekday_calc_tool


router = APIRouter(prefix="/api/weekday-calc", tags=["weekday-calc"])


class WeekdayRequest(BaseModel):
    dt: str


@router.post("/get-weekday")
async def get_weekday(request: WeekdayRequest):
    tool = get_weekday_calc_tool()
    dt = date.fromisoformat(request.dt)
    return {
        "weekday": tool.get_weekday(dt),
        "name_zh": tool.get_weekday_name(dt, "zh"),
        "name_en": tool.get_weekday_name(dt, "en")
    }


@router.post("/is-weekend")
async def is_weekend(request: WeekdayRequest):
    tool = get_weekday_calc_tool()
    dt = date.fromisoformat(request.dt)
    return {"is_weekend": tool.is_weekend(dt)}


class NextWeekdayRequest(BaseModel):
    dt: str
    target_weekday: int


@router.post("/next-weekday")
async def next_weekday(request: NextWeekdayRequest):
    tool = get_weekday_calc_tool()
    dt = date.fromisoformat(request.dt)
    return {"result": tool.next_weekday(dt, request.target_weekday).isoformat()}


class BusinessDaysRequest(BaseModel):
    start: str
    end: str


@router.post("/business-days")
async def business_days(request: BusinessDaysRequest):
    tool = get_weekday_calc_tool()
    start = date.fromisoformat(request.start)
    end = date.fromisoformat(request.end)
    return {"business_days": tool.business_days_between(start, end)}