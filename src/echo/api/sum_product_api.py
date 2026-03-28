"""求和与乘积API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.sum_product import get_sum_product_tool


router = APIRouter(prefix="/api/sum-product", tags=["sum-product"])


class MathRequest(BaseModel):
    numbers: List[float]


@router.post("/sum")
async def sum(request: MathRequest):
    tool = get_sum_product_tool()
    return {"result": tool.sum(request.numbers)}


@router.post("/product")
async def product(request: MathRequest):
    tool = get_sum_product_tool()
    return {"result": tool.product(request.numbers)}


@router.post("/average")
async def average(request: MathRequest):
    tool = get_sum_product_tool()
    return {"result": tool.average(request.numbers)}