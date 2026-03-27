"""Z分数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.z_score import get_z_score


router = APIRouter(prefix="/api/z-score", tags=["z-score"])


class ZScoreRequest(BaseModel):
    x: float
    mean: float
    stdev: float


@router.post("/calculate")
async def calculate(request: ZScoreRequest):
    return {"result": get_z_score().z_score(request.x, request.mean, request.stdev)}
