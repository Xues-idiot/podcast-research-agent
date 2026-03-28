"""随机种子API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.random_seed import get_random_seed_tool


router = APIRouter(prefix="/api/random-seed", tags=["random-seed"])


class SeedRequest(BaseModel):
    seed: int


class RandomRequest(BaseModel):
    start: int = 0
    end: int = 100


@router.post("/set-seed")
async def set_seed(request: SeedRequest):
    tool = get_random_seed_tool()
    tool.set_seed(request.seed)
    return {"message": "Seed set successfully"}


@router.post("/random")
async def get_random(request: RandomRequest):
    tool = get_random_seed_tool()
    return {"result": tool.get_random(request.start, request.end)}


@router.post("/random-float")
async def get_random_float():
    tool = get_random_seed_tool()
    return {"result": tool.get_random_float()}