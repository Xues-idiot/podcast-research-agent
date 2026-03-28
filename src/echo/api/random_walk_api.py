"""随机漫步API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.random_walk import get_random_walk_tool


router = APIRouter(prefix="/api/random-walk", tags=["random-walk"])


class Walk1DRequest(BaseModel):
    steps: int
    start: float = 0
    step_size: float = 1


@router.post("/walk-1d")
async def walk_1d(request: Walk1DRequest):
    tool = get_random_walk_tool()
    return {"result": tool.walk_1d(request.steps, request.start, request.step_size)}


class Walk2DRequest(BaseModel):
    steps: int
    start_x: float = 0
    start_y: float = 0


@router.post("/walk-2d")
async def walk_2d(request: Walk2DRequest):
    tool = get_random_walk_tool()
    return {"result": tool.walk_2d(request.steps, request.start_x, request.start_y)}


class GaussianRequest(BaseModel):
    steps: int
    start: float = 0
    std: float = 1


@router.post("/walk-gaussian")
async def walk_gaussian(request: GaussianRequest):
    tool = get_random_walk_tool()
    return {"result": tool.walk_gaussian(request.steps, request.start, request.std)}


class DistanceRequest(BaseModel):
    path: list


@router.post("/final-distance")
async def final_distance(request: DistanceRequest):
    tool = get_random_walk_tool()
    return {"result": tool.final_distance([tuple(p) for p in request.path])}