"""日期时间API路由"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.datetime_utils import dt_now, dt_today, dt_add, dt_diff, dt_format, dt_timestamp, dt_from_timestamp


class NowRequest(BaseModel):
    format: str = "%Y-%m-%d %H:%M:%S"


class AddRequest(BaseModel):
    dt_str: str
    days: int = 0
    hours: int = 0
    minutes: int = 0
    format: str = "%Y-%m-%d %H:%M:%S"


class DiffRequest(BaseModel):
    dt1_str: str
    dt2_str: str
    format: str = "%Y-%m-%d %H:%M:%S"


class FormatRequest(BaseModel):
    dt_str: str
    from_format: str
    to_format: str


class TimestampRequest(BaseModel):
    dt_str: str
    format: str = "%Y-%m-%d %H:%M:%S"


class FromTimestampRequest(BaseModel):
    timestamp: float


router = APIRouter(prefix="/api/datetime", tags=["datetime"])


@router.post("/now")
async def now(request: NowRequest) -> dict:
    result = dt_now(request.format)
    return {"result": result.result, "timestamp": result.timestamp}


@router.post("/today")
async def today(request: NowRequest) -> dict:
    result = dt_today(request.format)
    return {"result": result.result}


@router.post("/add")
async def add(request: AddRequest) -> dict:
    result = dt_add(request.dt_str, request.days, request.hours, request.minutes, request.format)
    return {"result": result.result, "timestamp": result.timestamp}


@router.post("/diff")
async def diff(request: DiffRequest) -> dict:
    return dt_diff(request.dt1_str, request.dt2_str, request.format)


@router.post("/format")
async def format(request: FormatRequest) -> dict:
    result = dt_format(request.dt_str, request.from_format, request.to_format)
    return {"result": result.result, "timestamp": result.timestamp}


@router.post("/timestamp")
async def timestamp(request: TimestampRequest) -> dict:
    return dt_timestamp(request.dt_str, request.format)


@router.post("/from-timestamp")
async def from_timestamp(request: FromTimestampRequest) -> dict:
    result = dt_from_timestamp(request.timestamp)
    return {"result": result.result}

