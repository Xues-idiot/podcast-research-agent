"""API统计API - 查看API使用统计"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.api_stats import get_api_stats


router = APIRouter(prefix="/api/stats", tags=["stats"])


class RecordCallRequest(BaseModel):
    """记录调用请求"""
    endpoint: str
    method: str
    status_code: int
    duration_ms: float
    user_id: str = ""
    ip: str = ""


@router.get("/")
async def get_stats():
    """获取统计摘要

    Returns:
        统计摘要
    """
    stats = get_api_stats()
    return stats.get_stats_summary()


@router.get("/recent")
async def get_recent_calls(limit: int = 100):
    """获取最近调用记录

    Args:
        limit: 数量限制

    Returns:
        最近调用列表
    """
    stats = get_api_stats()
    return {"calls": stats.get_recent_calls(limit=limit), "count": limit}


@router.get("/endpoints")
async def get_endpoint_stats(endpoint: str = None):
    """获取端点统计

    Args:
        endpoint: 端点路径

    Returns:
        端点统计
    """
    stats = get_api_stats()
    return stats.get_endpoint_stats(endpoint)


@router.get("/top")
async def get_top_endpoints(limit: int = 10, by: str = "calls"):
    """获取最常用端点

    Args:
        limit: 返回数量
        by: 排序方式 - calls, duration, errors

    Returns:
        端点列表
    """
    stats = get_api_stats()
    return {"endpoints": stats.get_top_endpoints(limit=limit, by=by)}


@router.get("/hourly")
async def get_hourly_stats(hours: int = 24):
    """获取小时统计

    Args:
        hours: 小时数

    Returns:
        小时统计数据
    """
    stats = get_api_stats()
    return {"hourly": stats.get_hourly_stats(hours=hours)}


@router.post("/record")
async def record_call(request: RecordCallRequest):
    """记录API调用

    Args:
        request: 调用信息

    Returns:
        记录结果
    """
    stats = get_api_stats()
    stats.record(
        endpoint=request.endpoint,
        method=request.method,
        status_code=request.status_code,
        duration_ms=request.duration_ms,
        user_id=request.user_id,
        ip=request.ip,
    )
    return {"status": "recorded"}


@router.post("/cleanup")
async def cleanup_old_calls(days: int = 7):
    """清除旧调用记录

    Args:
        days: 保留天数

    Returns:
        清理结果
    """
    stats = get_api_stats()
    removed = stats.clear_old_calls(days=days)
    return {"removed": removed}
