"""批量执行API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.batch_execute import get_batch_execute_tool


router = APIRouter(prefix="/api/batch-execute", tags=["batch-execute"])


class BatchRequest(BaseModel):
    items: List[Any]
    batch_size: int = 10


@router.post("/execute")
async def execute(request: BatchRequest):
    tool = get_batch_execute_tool()
    return {"message": "Batch execute configured", "item_count": len(request.items), "batch_size": request.batch_size}