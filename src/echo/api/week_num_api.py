"""周数计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.week_num import get_week_num_tool


router = APIRouter(prefix="/api/week-num", tags=["week-num"])


class WeekRequest(BaseModel):
    date_str: str


@router.post("/week-number")
async def week_number(request: WeekRequest):
    tool = get_week_num_tool()
    return {"week_number": tool.get_week_number(request.date_str)}


@router.post("/day-of-week")
async def day_of_week(request: WeekRequest):
    tool = get_week_num_tool()
    return {"day_of_week": tool.get_day_of_week(request.date_str)}