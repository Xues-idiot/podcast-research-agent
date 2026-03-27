"""分区API"""

from fastapi import APIRouter

from echo.research.partition_by import get_partition_by


router = APIRouter(prefix="/api/partition", tags=["partition"])


@router.post("/by")
async def partition_by(items: list, pred: str):
    """按条件分区"""
    tool = get_partition_by()
    pred_func = eval(pred)
    true_items, false_items = tool.partition_by(items, pred_func)
    return {"true": true_items, "false": false_items}


@router.post("/at")
async def partition_at(items: list, index: int):
    """在指定索引处分区"""
    tool = get_partition_by()
    left, right = tool.partition_at(items, index)
    return {"left": left, "right": right}
