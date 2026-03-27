"""序列API"""

from fastapi import APIRouter

from echo.research.sequencer import get_sequencer


router = APIRouter(prefix="/api/sequencer", tags=["sequencer"])


@router.post("/sequence")
async def sequence(start: int, stop: int, step: int = 1):
    return {"result": get_sequencer().sequence(start, stop, step)}