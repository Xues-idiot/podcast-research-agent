"""指数平滑API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.exponential_smoothing import get_exponential_smoothing


router = APIRouter(prefix="/api/exponential-smoothing", tags=["exponential-smoothing"])


class SmoothRequest(BaseModel):
    data: list
    alpha: float = 0.3


@router.post("/smooth")
async def smooth(request: SmoothRequest):
    return {"result": get_exponential_smoothing().smooth(request.data, request.alpha)}
