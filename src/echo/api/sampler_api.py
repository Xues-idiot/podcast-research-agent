"""采样API"""

from fastapi import APIRouter

from echo.research.sampler import get_sampler


router = APIRouter(prefix="/api/sampler", tags=["sampler"])


@router.post("/sample")
async def sample(items: list, count: int):
    return {"result": get_sampler().sample(items, count)}