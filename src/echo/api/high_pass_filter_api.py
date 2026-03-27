"""高通滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.high_pass_filter import get_high_pass_filter


router = APIRouter(prefix="/api/high-pass", tags=["high-pass"])


class FilterRequest(BaseModel):
    data: list
    alpha: float = 0.7


@router.post("/filter")
async def filter(request: FilterRequest):
    return {"result": get_high_pass_filter().filter(request.data, request.alpha)}
