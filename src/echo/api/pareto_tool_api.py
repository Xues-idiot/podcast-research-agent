"""帕累托API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.pareto_tool import get_pareto_tool


router = APIRouter(prefix="/api/pareto", tags=["pareto"])


class ParetoRequest(BaseModel):
    x: float
    alpha: float
    xm: float = 1


@router.post("/pdf")
async def pdf(request: ParetoRequest):
    return {"result": get_pareto_tool().pdf(request.x, request.alpha, request.xm)}
