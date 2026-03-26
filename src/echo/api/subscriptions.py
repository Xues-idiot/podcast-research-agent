"""订阅API - 管理播客订阅"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.subscriptions import (
    SubscriptionStatus,
    get_subscription_manager,
)


router = APIRouter(prefix="/api/subscriptions", tags=["subscriptions"])


class AddSubscriptionRequest(BaseModel):
    """添加订阅请求"""
    url: str
    title: str = ""
    feed_url: str = ""
    platform: str = ""
    update_interval_hours: int = 24
    auto_research: bool = False


class UpdateSubscriptionRequest(BaseModel):
    """更新订阅请求"""
    title: Optional[str] = None
    status: Optional[str] = None  # active, paused, error
    update_interval_hours: Optional[int] = None
    auto_research: Optional[bool] = None


@router.get("/")
async def list_subscriptions(
    status: Optional[str] = None,
    platform: Optional[str] = None,
):
    """列出所有订阅

    Args:
        status: 按状态筛选 (active, paused, error)
        platform: 按平台筛选

    Returns:
        订阅列表
    """
    manager = get_subscription_manager()
    sub_status = SubscriptionStatus(status) if status else None
    subscriptions = manager.list(status=sub_status, platform=platform)
    return {
        "subscriptions": [s.to_dict() for s in subscriptions],
        "count": len(subscriptions),
    }


@router.post("/")
async def add_subscription(request: AddSubscriptionRequest):
    """添加订阅

    Args:
        request: 订阅信息

    Returns:
        创建的订阅
    """
    manager = get_subscription_manager()
    subscription = manager.add(
        url=request.url,
        title=request.title,
        feed_url=request.feed_url,
        platform=request.platform,
        update_interval_hours=request.update_interval_hours,
        auto_research=request.auto_research,
    )
    return subscription.to_dict()


@router.get("/{subscription_id}")
async def get_subscription(subscription_id: str):
    """获取订阅详情

    Args:
        subscription_id: 订阅ID

    Returns:
        订阅详情
    """
    manager = get_subscription_manager()
    subscription = manager.get(subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription.to_dict()


@router.put("/{subscription_id}")
async def update_subscription(
    subscription_id: str,
    request: UpdateSubscriptionRequest,
):
    """更新订阅配置

    Args:
        subscription_id: 订阅ID
        request: 更新内容

    Returns:
        更新后的订阅
    """
    manager = get_subscription_manager()
    updates = {}
    if request.title is not None:
        updates["title"] = request.title
    if request.status is not None:
        updates["status"] = SubscriptionStatus(request.status)
    if request.update_interval_hours is not None:
        updates["update_interval_hours"] = request.update_interval_hours
    if request.auto_research is not None:
        updates["auto_research"] = request.auto_research

    if not manager.update(subscription_id, **updates):
        raise HTTPException(status_code=404, detail="Subscription not found")

    subscription = manager.get(subscription_id)
    return subscription.to_dict()


@router.delete("/{subscription_id}")
def remove_subscription(subscription_id: str):
    """移除订阅

    Args:
        subscription_id: 订阅ID

    Returns:
        操作结果
    """
    manager = get_subscription_manager()
    if not manager.remove(subscription_id):
        raise HTTPException(status_code=404, detail="Subscription not found")
    return {"status": "removed", "subscription_id": subscription_id}


@router.post("/{subscription_id}/check")
async def check_updates(subscription_id: str):
    """检查订阅更新

    Args:
        subscription_id: 订阅ID

    Returns:
        新剧集列表
    """
    manager = get_subscription_manager()
    subscription = manager.get(subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    new_episodes = manager.check_updates(subscription_id)
    return {
        "subscription_id": subscription_id,
        "new_episodes": [
            {
                "id": ep.id,
                "title": ep.title,
                "url": ep.url,
                "published_at": ep.published_at,
                "duration": ep.duration,
            }
            for ep in new_episodes
        ],
        "count": len(new_episodes),
    }


@router.get("/{subscription_id}/episodes")
async def get_episodes(subscription_id: str):
    """获取订阅的所有剧集

    Args:
        subscription_id: 订阅ID

    Returns:
        剧集列表
    """
    manager = get_subscription_manager()
    subscription = manager.get(subscription_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")

    episodes = manager.get_episodes(subscription_id)
    return {
        "subscription_id": subscription_id,
        "episodes": [
            {
                "id": ep.id,
                "title": ep.title,
                "url": ep.url,
                "published_at": ep.published_at,
                "duration": ep.duration,
                "is_new": ep.is_new,
                "research_status": ep.research_status,
            }
            for ep in episodes
        ],
        "count": len(episodes),
    }
