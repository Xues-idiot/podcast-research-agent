"""截断平均API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.trimmed_mean import get_trimmed_mean


router = APIRouter(prefix="/api/trimmed-mean", tags=["trimmed-mean"])


class TrimmedMeanRequest(BaseModel):
    data: list
    proportion: float = 0.1


@router.post("/calculate")
async def calculate(request: TrimmedMeanRequest):
    return {"result": get_trimmed_mean().trimmed_mean(request.data, request.proportion)}
