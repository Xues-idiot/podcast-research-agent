"""均匀分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.Uniform_distribution import get_uniform_distribution


router = APIRouter(prefix="/api/uniform", tags=["uniform"])


class UniformRequest(BaseModel):
    x: float
    a: float
    b: float


@router.post("/pdf")
async def pdf(request: UniformRequest):
    return {"result": get_uniform_distribution().pdf(request.x, request.a, request.b)}
