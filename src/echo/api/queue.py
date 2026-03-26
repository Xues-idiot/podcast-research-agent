"""队列API - 管理研究任务队列"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.queue import (
    QueueStatus,
    QueuePriority,
    get_research_queue,
)


router = APIRouter(prefix="/api/queue", tags=["queue"])


class AddQueueRequest(BaseModel):
    """添加队列请求"""
    url: str
    title: str = ""
    priority: int = 2  # 1=low, 2=normal, 3=high, 4=urgent


class UpdateProgressRequest(BaseModel):
    """更新进度请求"""
    progress: float


@router.get("/")
async def list_queue(status: Optional[str] = None, limit: int = 50):
    """列出队列

    Args:
        status: 状态筛选
        limit: 数量限制

    Returns:
        队列列表
    """
    queue = get_research_queue()

    qstatus = None
    if status:
        try:
            qstatus = QueueStatus(status)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid status: {status}")

    items = queue.list(status=qstatus, limit=limit)
    return {
        "items": [
            {
                **item.__dict__,
                "status": item.status.value,
                "priority": item.priority.value,
            }
            for item in items
        ],
        "count": len(items),
        "stats": queue.get_stats(),
    }


@router.post("/")
async def add_to_queue(request: AddQueueRequest):
    """添加队列项

    Args:
        request: 队列项信息

    Returns:
        添加的队列项
    """
    queue = get_research_queue()

    try:
        priority = QueuePriority(request.priority)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid priority: {request.priority}")

    item = queue.add(
        url=request.url,
        title=request.title,
        priority=priority,
    )

    return {
        **item.__dict__,
        "status": item.status.value,
        "priority": item.priority.value,
    }


@router.post("/{item_id}/cancel")
async def cancel_item(item_id: str):
    """取消队列项

    Args:
        item_id: 队列项ID

    Returns:
        操作结果
    """
    queue = get_research_queue()
    if not queue.cancel(item_id):
        raise HTTPException(status_code=404, detail="Queue item not found or not cancellable")
    return {"status": "cancelled", "item_id": item_id}


@router.post("/{item_id}/retry")
async def retry_item(item_id: str):
    """重试失败的队列项

    Args:
        item_id: 队列项ID

    Returns:
        操作结果
    """
    queue = get_research_queue()
    if not queue.retry(item_id):
        raise HTTPException(status_code=404, detail="Queue item not found or not retryable")
    return {"status": "retried", "item_id": item_id}


@router.delete("/{item_id}")
def remove_item(item_id: str):
    """移除队列项

    Args:
        item_id: 队列项ID

    Returns:
        操作结果
    """
    queue = get_research_queue()
    if not queue.remove(item_id):
        raise HTTPException(status_code=404, detail="Queue item not found")
    return {"status": "removed", "item_id": item_id}


@router.post("/clear-completed")
async def clear_completed():
    """清除已完成的项

    Returns:
        操作结果
    """
    queue = get_research_queue()
    queue.clear_completed()
    return {"status": "cleared"}


@router.get("/stats")
async def get_stats():
    """获取队列统计

    Returns:
        队列统计
    """
    queue = get_research_queue()
    return queue.get_stats()


@router.post("/stop")
async def stop_queue():
    """停止队列处理

    Returns:
        操作结果
    """
    queue = get_research_queue()
    queue.stop()
    return {"status": "stopped"}
