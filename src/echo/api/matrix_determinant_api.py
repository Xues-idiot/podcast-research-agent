"""矩阵行列式API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.matrix_determinant import get_matrix_determinant_tool


router = APIRouter(prefix="/api/matrix-determinant", tags=["matrix-determinant"])


class DeterminantRequest(BaseModel):
    matrix: list[list[float]]


@router.post("/determinant")
async def determinant(request: DeterminantRequest):
    tool = get_matrix_determinant_tool()
    return {"result": tool.determinant(request.matrix)}