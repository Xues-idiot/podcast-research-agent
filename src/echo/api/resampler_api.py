"""重采样API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.resampler import get_resampler


router = APIRouter(prefix="/api/resample", tags=["resample"])


class ResampleRequest(BaseModel):
    signal: list
    factor: int


@router.post("/up")
async def up(request: ResampleRequest):
    return {"result": get_resampler().upsample(request.signal, request.factor)}
