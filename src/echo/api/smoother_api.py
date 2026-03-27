"""平滑API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.smoother import get_smoother


router = APIRouter(prefix="/api/smoother", tags=["smoother"])


class SmootherRequest(BaseModel):
    data: list
    window: int


@router.post("/moving-average")
async def moving_average(request: SmootherRequest):
    return {"result": get_smoother().moving_average(request.data, request.window)}
