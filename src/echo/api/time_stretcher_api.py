"""时间拉伸API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.time_stretcher import get_time_stretcher


router = APIRouter(prefix="/api/time-stretch", tags=["time-stretch"])


class StretchRequest(BaseModel):
    signal: list
    factor: float


@router.post("/stretch")
async def stretch(request: StretchRequest):
    return {"result": get_time_stretcher().stretch(request.signal, request.factor)}
