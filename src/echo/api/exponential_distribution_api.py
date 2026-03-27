"""指数分布API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.exponential_distribution import get_exponential_distribution


router = APIRouter(prefix="/api/exponential-dist", tags=["exponential-dist"])


class ExponentialRequest(BaseModel):
    x: float
    lambda_val: float


@router.post("/pdf")
async def pdf(request: ExponentialRequest):
    return {"result": get_exponential_distribution().pdf(request.x, request.lambda_val)}
