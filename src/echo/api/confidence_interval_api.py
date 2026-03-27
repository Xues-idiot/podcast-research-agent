"""置信区间API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.clopper_pearson import get_confidence_interval


router = APIRouter(prefix="/api/confidence-interval", tags=["confidence-interval"])


class ConfidenceRequest(BaseModel):
    mean: float
    stdev: float
    n: int
    confidence: float = 0.95


@router.post("/calculate")
async def calculate(request: ConfidenceRequest):
    return {"result": get_confidence_interval().confidence_interval(
        request.mean, request.stdev, request.n, request.confidence
    )}
