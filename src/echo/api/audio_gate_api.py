"""音频噪声门API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.audio_gate import get_audio_gate_tool


router = APIRouter(prefix="/api/audio-gate", tags=["audio-gate"])


class GateRequest(BaseModel):
    signal: list[float]
    threshold: float = 0.1


@router.post("/gate")
async def gate(request: GateRequest):
    tool = get_audio_gate_tool()
    return {"result": tool.gate(request.signal, request.threshold)}