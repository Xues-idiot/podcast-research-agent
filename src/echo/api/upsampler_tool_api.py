"""升采样API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.upsampler_tool import get_upsampler_tool


router = APIRouter(prefix="/api/upsample", tags=["upsample"])


class UpsampleRequest(BaseModel):
    signal: list
    factor: int


@router.post("/up")
async def up(request: UpsampleRequest):
    return {"result": get_upsampler_tool().upsample(request.signal, request.factor)}
