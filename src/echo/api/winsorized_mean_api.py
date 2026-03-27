"""Winsorized平均API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.winsorized_mean import get_winsorized_mean


router = APIRouter(prefix="/api/winsorized-mean", tags=["winsorized-mean"])


class WinsorizedRequest(BaseModel):
    data: list
    proportion: float = 0.1


@router.post("/calculate")
async def calculate(request: WinsorizedRequest):
    return {"result": get_winsorized_mean().winsorized_mean(request.data, request.proportion)}
