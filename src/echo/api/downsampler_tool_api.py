"""降采样API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.downsampler_tool import get_downsampler_tool


router = APIRouter(prefix="/api/downsample", tags=["downsample"])


class DownsampleRequest(BaseModel):
    signal: list
    factor: int


@router.post("/down")
async def down(request: DownsampleRequest):
    return {"result": get_downsampler_tool().downsample(request.signal, request.factor)}
