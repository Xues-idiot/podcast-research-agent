"""音频音高变换API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_pitch_shift import get_audio_pitch_shift_tool


router = APIRouter(prefix="/api/audio-pitch-shift", tags=["audio-pitch-shift"])


class PitchShiftRequest(BaseModel):
    signal: list[float]
    semitones: float = 0.0


@router.post("/pitch-shift")
async def pitch_shift(request: PitchShiftRequest):
    tool = get_audio_pitch_shift_tool()
    return {"result": tool.pitch_shift(request.signal, request.semitones)}