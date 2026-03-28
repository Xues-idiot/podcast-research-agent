"""向量运算API"""

from fastapi import APIRouter

from echo.research.vector_ops import get_vector_ops


router = APIRouter(prefix="/api/vector", tags=["vector"])


@router.post("/dot")
async def dot_product(a: list[float], b: list[float]):
    ops = get_vector_ops()
    return {"result": ops.dot(a, b)}
