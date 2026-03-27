"""相干函数API"""

from fastapi import APIRouter

from echo.research.coherence_function import get_coherence_function


router = APIRouter(prefix="/api/coherence", tags=["coherence"])


@router.post("/compute")
async def compute(signal1: list, signal2: list):
    return {"result": get_coherence_function().coherence(signal1, signal2)}
