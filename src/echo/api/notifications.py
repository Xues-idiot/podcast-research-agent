"""通知API - 管理用户通知"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.notifications import (
    NotificationManager,
    NotificationType,
    NotificationPriority,
    get_notification_manager,
)


router = APIRouter(prefix="/api/notifications", tags=["notifications"])


class SendNotificationRequest(BaseModel):
    """发送通知请求"""
    type: str
    title: str
    message: str
    priority: str = "normal"
    data: dict = {}


class UpdateSettingsRequest(BaseModel):
    """更新设置请求"""
    enabled: Optional[bool] = None
    research_completed: Optional[bool] = None
    new_episode: Optional[bool] = None
    subscription_update: Optional[bool] = None
    share_accessed: Optional[bool] = None
    weekly_summary: Optional[bool] = None
    quiet_hours_start: Optional[str] = None
    quiet_hours_end: Optional[str] = None
    max_notifications: Optional[int] = None


@router.get("/")
async def list_notifications(
    unread_only: bool = False,
    notif_type: Optional[str] = None,
    limit: int = 50,
):
    """列出通知

    Args:
        unread_only: 只返回未读
        notif_type: 通知类型筛选
        limit: 数量限制

    Returns:
        通知列表
    """
    manager = get_notification_manager()

    ntype = None
    if notif_type:
        try:
            ntype = NotificationType(notif_type)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid notification type: {notif_type}")

    notifications = manager.list(
        unread_only=unread_only,
        notif_type=ntype,
        limit=limit,
    )

    return {
        "notifications": [
            {
                **n.__dict__,
                "type": n.type.value,
                "priority": n.priority.value,
            }
            for n in notifications
        ],
        "count": len(notifications),
        "unread_count": manager.get_unread_count(),
    }


@router.post("/")
async def send_notification(request: SendNotificationRequest):
    """发送通知

    Args:
        request: 通知信息

    Returns:
        发送结果
    """
    manager = get_notification_manager()

    try:
        ntype = NotificationType(request.type)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid notification type: {request.type}")

    try:
        priority = NotificationPriority(request.priority)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Invalid priority: {request.priority}")

    notification = manager.send(
        notif_type=ntype,
        title=request.title,
        message=request.message,
        priority=priority,
        data=request.data,
    )

    if not notification:
        return {"status": "skipped", "reason": "notification disabled"}

    return {
        "status": "sent",
        "notification": {
            **notification.__dict__,
            "type": notification.type.value,
            "priority": notification.priority.value,
        },
    }


@router.post("/read/{notification_id}")
async def mark_read(notification_id: str):
    """标记已读

    Args:
        notification_id: 通知ID

    Returns:
        操作结果
    """
    manager = get_notification_manager()
    if not manager.mark_read(notification_id):
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"status": "marked_read", "notification_id": notification_id}


@router.post("/read-all")
async def mark_all_read():
    """标记所有已读

    Returns:
        操作结果
    """
    manager = get_notification_manager()
    count = manager.mark_all_read()
    return {"status": "marked_read", "count": count}


@router.delete("/{notification_id}")
def delete_notification(notification_id: str):
    """删除通知

    Args:
        notification_id: 通知ID

    Returns:
        操作结果
    """
    manager = get_notification_manager()
    if not manager.delete(notification_id):
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"status": "deleted", "notification_id": notification_id}


@router.post("/clear")
async def clear_all():
    """清除所有通知

    Returns:
        操作结果
    """
    manager = get_notification_manager()
    manager.clear_all()
    return {"status": "cleared"}


@router.get("/settings")
async def get_settings():
    """获取通知设置

    Returns:
        通知设置
    """
    manager = get_notification_manager()
    return manager.get_settings()


@router.put("/settings")
def update_settings(request: UpdateSettingsRequest):
    """更新通知设置

    Args:
        request: 设置更新

    Returns:
        更新后的设置
    """
    manager = get_notification_manager()

    settings = {}
    if request.enabled is not None:
        settings["enabled"] = request.enabled
    if request.research_completed is not None:
        settings["research_completed"] = request.research_completed
    if request.new_episode is not None:
        settings["new_episode"] = request.new_episode
    if request.subscription_update is not None:
        settings["subscription_update"] = request.subscription_update
    if request.share_accessed is not None:
        settings["share_accessed"] = request.share_accessed
    if request.weekly_summary is not None:
        settings["weekly_summary"] = request.weekly_summary
    if request.quiet_hours_start is not None:
        settings["quiet_hours_start"] = request.quiet_hours_start
    if request.quiet_hours_end is not None:
        settings["quiet_hours_end"] = request.quiet_hours_end
    if request.max_notifications is not None:
        settings["max_notifications"] = request.max_notifications

    return manager.update_settings(settings)


@router.get("/summary/weekly")
async def get_weekly_summary():
    """获取周报

    Returns:
        周报数据
    """
    manager = get_notification_manager()
    return manager.get_weekly_summary()
