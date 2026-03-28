"""样本数据生成API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.sample_data import get_sample_data_tool


router = APIRouter(prefix="/api/sample-data", tags=["sample-data"])


class RandomIntsRequest(BaseModel):
    count: int
    min_val: int = 0
    max_val: int = 100


@router.post("/random-ints")
async def random_ints(request: RandomIntsRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_ints(request.count, request.min_val, request.max_val)}


class RandomFloatsRequest(BaseModel):
    count: int
    min_val: float = 0
    max_val: float = 1


@router.post("/random-floats")
async def random_floats(request: RandomFloatsRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_floats(request.count, request.min_val, request.max_val)}


class RandomStringsRequest(BaseModel):
    count: int
    length: int = 10


@router.post("/random-strings")
async def random_strings(request: RandomStringsRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_strings(request.count, request.length)}


class RandomDatesRequest(BaseModel):
    count: int
    start_year: int = 2020
    end_year: int = 2024


@router.post("/random-dates")
async def random_dates(request: RandomDatesRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_dates(request.count, request.start_year, request.end_year)}


@router.post("/random-emails")
async def random_emails(request: RandomIntsRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_emails(request.count)}


@router.post("/random-ips")
async def random_ips(request: RandomIntsRequest):
    tool = get_sample_data_tool()
    return {"result": tool.random_ips(request.count)}