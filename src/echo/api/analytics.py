"""分析统计API - 查看使用统计数据"""

from fastapi import APIRouter

from echo.research.analytics import get_analytics_manager


router = APIRouter(prefix="/api/analytics", tags=["analytics"])


@router.get("/stats")
async def get_stats(days: int = 30):
    """获取使用统计

    Args:
        days: 统计天数

    Returns:
        使用统计数据
    """
    manager = get_analytics_manager()
    stats = manager.get_stats(days=days)
    return stats.to_dict()


@router.get("/daily")
async def get_daily_stats(days: int = 7):
    """获取每日统计

    Args:
        days: 天数

    Returns:
        每日统计数据
    """
    manager = get_analytics_manager()
    return {"daily": manager.get_daily_stats(days=days)}


@router.get("/platforms")
async def get_platform_stats():
    """获取平台统计

    Returns:
        平台统计数据
    """
    manager = get_analytics_manager()
    return {"platforms": manager.get_platform_stats()}


@router.get("/recent")
async def get_recent_activity(limit: int = 20):
    """获取最近活动

    Args:
        limit: 返回数量

    Returns:
        最近活动列表
    """
    manager = get_analytics_manager()
    return {"recent": manager.get_recent_activity(limit=limit)}


@router.get("/streak")
async def get_streak():
    """获取连续活跃天数

    Returns:
        连续活跃统计数据
    """
    manager = get_analytics_manager()
    return manager.get_streak()


@router.post("/track")
async def track_event(
    research_id: str,
    event_type: str,
    source: str = "",
    platform: str = "",
    duration_seconds: float = 0.0,
    keypoints_count: int = 0,
):
    """跟踪研究事件

    Args:
        research_id: 研究ID
        event_type: 事件类型
        source: 来源
        platform: 平台
        duration_seconds: 耗时
        keypoints_count: 要点数

    Returns:
        跟踪结果
    """
    manager = get_analytics_manager()
    manager.track(
        research_id=research_id,
        event_type=event_type,
        source=source,
        platform=platform,
        duration_seconds=duration_seconds,
        keypoints_count=keypoints_count,
    )
    return {"status": "tracked"}


@router.post("/cleanup")
async def cleanup_old_events(days: int = 90):
    """清理旧事件

    Args:
        days: 保留天数

    Returns:
        清理结果
    """
    manager = get_analytics_manager()
    removed = manager.clear_old_events(days=days)
    return {"removed": removed}
