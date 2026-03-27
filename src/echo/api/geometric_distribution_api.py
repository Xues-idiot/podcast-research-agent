"""几何分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.geometric_distribution import get_geometric_distribution


router = APIRouter(prefix="/api/geometric", tags=["geometric"])


class GeometricRequest(BaseModel):
    k: int
    p: float


@router.post("/pmf")
async def pmf(request: GeometricRequest):
    return {"result": get_geometric_distribution().pmf(request.k, request.p)}
