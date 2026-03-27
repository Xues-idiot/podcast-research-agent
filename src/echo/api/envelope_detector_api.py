"""包络检测API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.envelope_detector import get_envelope_detector


router = APIRouter(prefix="/api/envelope", tags=["envelope"])


class EnvelopeRequest(BaseModel):
    signal: list
    alpha: float = 0.1


@router.post("/detect")
async def detect(request: EnvelopeRequest):
    return {"result": get_envelope_detector().detect(request.signal, request.alpha)}
