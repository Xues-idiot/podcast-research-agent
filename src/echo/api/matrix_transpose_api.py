"""矩阵转置API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_transpose import get_matrix_transpose_tool


router = APIRouter(prefix="/api/matrix-transpose", tags=["matrix-transpose"])


class TransposeRequest(BaseModel):
    matrix: list[list[float]]


@router.post("/transpose")
async def transpose(request: TransposeRequest):
    tool = get_matrix_transpose_tool()
    return {"result": tool.transpose(request.matrix)}