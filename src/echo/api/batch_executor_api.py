"""批处理执行器API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.batch_executor import get_batch_executor


router = APIRouter(prefix="/api/batch-executor", tags=["batch-executor"])


class BatchRequest(BaseModel):
    tasks: list
    batch_size: int = 10


@router.post("/execute")
async def execute(request: BatchRequest):
    return {"result": []}
