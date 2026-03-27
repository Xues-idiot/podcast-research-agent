"""并行执行器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.parallel_executor import get_parallel_executor


router = APIRouter(prefix="/api/parallel", tags=["parallel"])


class ParallelRequest(BaseModel):
    funcs: list
    max_workers: int = 4


@router.post("/execute")
async def execute(request: ParallelRequest):
    return {"result": []}
