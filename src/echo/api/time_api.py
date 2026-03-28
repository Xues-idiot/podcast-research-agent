"""时间工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.time_utils import time_now, time_today, time_timestamp, time_from_timestamp, time_add, time_diff, time_format


class NowRequest(BaseModel):
    pass


class AddRequest(BaseModel):
    dt_str: str
    days: int = 0
    hours: int = 0
    minutes: int = 0


class DiffRequest(BaseModel):
    dt1_str: str
    dt2_str: str


class FormatRequest(BaseModel):
    dt_str: str
    fmt: str


router = APIRouter(prefix="/api/time", tags=["time"])


@router.post("/now")
async def now() -> dict:
    return {"result": time_now()}


@router.post("/today")
async def today() -> dict:
    return {"result": time_today()}


@router.post("/timestamp")
async def timestamp() -> dict:
    return {"result": time_timestamp()}


@router.post("/from-timestamp")
async def from_timestamp(request: NowRequest) -> dict:
    return {"result": time_from_timestamp(time_timestamp())}


@router.post("/add")
async def add(request: AddRequest) -> dict:
    return {"result": time_add(request.dt_str, request.days, request.hours, request.minutes)}


@router.post("/diff")
async def diff(request: DiffRequest) -> dict:
    return time_diff(request.dt1_str, request.dt2_str)


@router.post("/format")
async def format(request: FormatRequest) -> dict:
    return {"result": time_format(request.dt_str, request.fmt)}
