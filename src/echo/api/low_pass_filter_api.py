"""低通滤波API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.low_pass_filter import get_low_pass_filter


router = APIRouter(prefix="/api/low-pass", tags=["low-pass"])


class FilterRequest(BaseModel):
    data: list
    alpha: float = 0.3


@router.post("/filter")
async def filter(request: FilterRequest):
    return {"result": get_low_pass_filter().filter(request.data, request.alpha)}
