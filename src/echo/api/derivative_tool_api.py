"""导数API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.derivative_tool import get_derivative_tool


router = APIRouter(prefix="/api/derivative-tool", tags=["derivative-tool"])


class DerivativeRequest(BaseModel):
    points: list
    dt: float = 1.0


@router.post("/derivative")
async def derivative(request: DerivativeRequest):
    return {"result": get_derivative_tool().derivative(request.points, request.dt)}
