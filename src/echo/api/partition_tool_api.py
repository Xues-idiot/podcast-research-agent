"""分区工具API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.partition_tool import get_partition_tool


router = APIRouter(prefix="/api/partition", tags=["partition"])


class PartitionRequest(BaseModel):
    items: list
    pred: str = "lambda x: x"


@router.post("/partition")
async def partition(request: PartitionRequest):
    pred = eval(request.pred)
    true_list, false_list = get_partition_tool().partition(request.items, pred)
    return {"true": true_list, "false": false_list}
