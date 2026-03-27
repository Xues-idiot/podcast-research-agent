"""贝叶斯推断API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.bayesian_tool import get_bayesian_tool


router = APIRouter(prefix="/api/bayesian", tags=["bayesian"])


class BayesRequest(BaseModel):
    prior: float
    likelihood: float
    marginal: float


@router.post("/posterior")
async def posterior(request: BayesRequest):
    return {"result": get_bayesian_tool().posterior(
        request.prior, request.likelihood, request.marginal
    )}
