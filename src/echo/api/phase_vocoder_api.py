"""相位声码器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.phase_vocoder import get_phase_vocoder


router = APIRouter(prefix="/api/phase-vocoder", tags=["phase-vocoder"])


class VocoderRequest(BaseModel):
    signal: list
    stretch_factor: float


@router.post("/vocode")
async def vocode(request: VocoderRequest):
    return {"result": get_phase_vocoder().phase_vocode(request.signal, request.stretch_factor)}
