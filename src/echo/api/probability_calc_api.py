"""概率计算API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from echo.research.probability_calc import get_probability_calc_tool


router = APIRouter(prefix="/api/probability-calc", tags=["probability-calc"])


@router.post("/factorial")
async def factorial(request: BaseModel):
    tool = get_probability_calc_tool()
    return {"result": tool.factorial(request.get("n", 0))}


class PermutationRequest(BaseModel):
    n: int
    r: int


@router.post("/permutation")
async def permutation(request: PermutationRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.permutation(request.n, request.r)}


class CombinationRequest(BaseModel):
    n: int
    r: int


@router.post("/combination")
async def combination(request: CombinationRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.combination(request.n, request.r)}


class BinomialRequest(BaseModel):
    n: int
    k: int
    p: float


@router.post("/binomial")
async def binomial_prob(request: BinomialRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.binomial_prob(request.n, request.k, request.p)}


class NormalRequest(BaseModel):
    x: float
    mean: float = 0
    std: float = 1


@router.post("/normal-cdf")
async def normal_cdf(request: NormalRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.normal_cdf(request.x, request.mean, request.std)}


class PoissonRequest(BaseModel):
    k: int
    lambda_: float


@router.post("/poisson")
async def poisson_prob(request: PoissonRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.poisson_prob(request.k, request.lambda_)}


class EVRequest(BaseModel):
    values: List[float]
    probabilities: List[float]


@router.post("/expected-value")
async def expected_value(request: EVRequest):
    tool = get_probability_calc_tool()
    return {"result": tool.expected_value(request.values, request.probabilities)}