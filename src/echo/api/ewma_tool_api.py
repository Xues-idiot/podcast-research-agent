"""指数加权移动平均API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.ewma_tool import get_ewma_tool


router = APIRouter(prefix="/api/ewma", tags=["ewma"])


class EwmaRequest(BaseModel):
    data: list
    alpha: float = 0.3


@router.post("/calculate")
async def calculate(request: EwmaRequest):
    return {"result": get_ewma_tool().ewma(request.data, request.alpha)}
