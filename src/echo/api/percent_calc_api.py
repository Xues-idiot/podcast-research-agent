"""百分比计算API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.percent_calc import get_percent_calc_tool


router = APIRouter(prefix="/api/percent-calc", tags=["percent-calc"])


class CalculateRequest(BaseModel):
    part: float
    whole: float


@router.post("/calculate")
async def calculate(request: CalculateRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.calculate(request.part, request.whole)}


class OfRequest(BaseModel):
    percent: float
    whole: float


@router.post("/of")
async def of_value(request: OfRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.of(request.percent, request.whole)}


class ChangeRequest(BaseModel):
    old_val: float
    new_val: float


@router.post("/change")
async def change(request: ChangeRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.change(request.old_val, request.new_val)}


class IncreaseRequest(BaseModel):
    original: float
    percent: float


@router.post("/increase")
async def increase(request: IncreaseRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.increase(request.original, request.percent)}


class DecreaseRequest(BaseModel):
    original: float
    percent: float


@router.post("/decrease")
async def decrease(request: DecreaseRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.decrease(request.original, request.percent)}


class ReverseRequest(BaseModel):
    reduced_val: float
    percent: float


@router.post("/reverse")
async def reverse(request: ReverseRequest):
    tool = get_percent_calc_tool()
    return {"result": tool.reverse(request.reduced_val, request.percent)}