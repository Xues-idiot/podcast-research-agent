"""信号插值API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.interpolator_signal import get_signal_interpolator


router = APIRouter(prefix="/api/signal-interp", tags=["signal-interp"])


class InterpRequest(BaseModel):
    signal: list
    factor: int


@router.post("/interpolate")
async def interpolate(request: InterpRequest):
    return {"result": get_signal_interpolator().interpolate(request.signal, request.factor)}
