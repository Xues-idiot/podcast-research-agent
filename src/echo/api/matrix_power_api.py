"""矩阵幂API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_power import get_matrix_power_tool


router = APIRouter(prefix="/api/matrix-power", tags=["matrix-power"])


class PowerRequest(BaseModel):
    matrix: list[list[float]]
    n: int


@router.post("/power")
async def power(request: PowerRequest):
    tool = get_matrix_power_tool()
    return {"result": tool.power(request.matrix, request.n)}