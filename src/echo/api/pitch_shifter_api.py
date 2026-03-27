"""音高变换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pitch_shifter import get_pitch_shifter


router = APIRouter(prefix="/api/pitch-shift", tags=["pitch-shift"])


class PitchRequest(BaseModel):
    signal: list
    semitones: int


@router.post("/shift")
async def shift(request: PitchRequest):
    return {"result": get_pitch_shifter().shift(request.signal, request.semitones)}
