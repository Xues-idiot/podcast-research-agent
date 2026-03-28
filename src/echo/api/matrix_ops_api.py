"""矩阵运算API"""

from fastapi import APIRouter

from echo.research.matrix_ops import get_matrix_ops


router = APIRouter(prefix="/api/matrix", tags=["matrix"])


@router.post("/multiply")
async def multiply_matrices(a: list[list[float]], b: list[list[float]]):
    ops = get_matrix_ops()
    return {"result": ops.multiply(a, b)}
