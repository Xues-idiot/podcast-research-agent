"""矩阵求逆API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_inverse import get_matrix_inverse_tool


router = APIRouter(prefix="/api/matrix-inverse", tags=["matrix-inverse"])


class InverseRequest(BaseModel):
    matrix: list[list[float]]


@router.post("/inverse")
async def inverse(request: InverseRequest):
    tool = get_matrix_inverse_tool()
    return {"result": tool.inverse(request.matrix)}