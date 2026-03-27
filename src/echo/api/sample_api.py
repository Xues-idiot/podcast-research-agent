"""采样API"""

from fastapi import APIRouter

from echo.research.sample_tool import get_sample_tool


router = APIRouter(prefix="/api/sample", tags=["sample"])


@router.post("/sample")
async def sample(items: list, count: int):
    return {"result": get_sample_tool().sample(items, count)}