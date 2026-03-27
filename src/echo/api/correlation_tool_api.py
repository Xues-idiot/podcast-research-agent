"""相关性API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.correlation_tool import get_correlation_tool


router = APIRouter(prefix="/api/correlation", tags=["correlation"])


class CorrelationRequest(BaseModel):
    x: list
    y: list


@router.post("/pearson")
async def pearson(request: CorrelationRequest):
    return {"result": get_correlation_tool().pearson(request.x, request.y)}
