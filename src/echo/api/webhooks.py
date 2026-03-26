"""Webhook API - 管理Webhook配置"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.webhooks import (
    WebhookEvent,
    get_webhook_manager,
)


router = APIRouter(prefix="/api/webhooks", tags=["webhooks"])


class AddWebhookRequest(BaseModel):
    """添加Webhook请求"""
    url: str
    events: list[str]  # 事件类型列表
    secret: str = ""


class UpdateWebhookRequest(BaseModel):
    """更新Webhook请求"""
    url: Optional[str] = None
    events: Optional[list[str]] = None
    secret: Optional[str] = None
    active: Optional[bool] = None


@router.get("/")
async def list_webhooks(active_only: bool = False):
    """列出所有Webhook

    Args:
        active_only: 只返回活跃的Webhook

    Returns:
        Webhook列表
    """
    manager = get_webhook_manager()
    webhooks = manager.list(active_only=active_only)
    return {
        "webhooks": [w.to_dict() for w in webhooks],
        "count": len(webhooks),
    }


@router.post("/")
async def add_webhook(request: AddWebhookRequest):
    """添加Webhook

    Args:
        request: Webhook配置

    Returns:
        创建的Webhook
    """
    # 验证事件类型
    for event in request.events:
        try:
            WebhookEvent(event)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid event type: {event}",
            )

    manager = get_webhook_manager()
    webhook = manager.add(
        url=request.url,
        events=request.events,
        secret=request.secret,
    )
    return webhook.to_dict()


@router.get("/{webhook_id}")
async def get_webhook(webhook_id: str):
    """获取Webhook详情

    Args:
        webhook_id: Webhook ID

    Returns:
        Webhook详情
    """
    manager = get_webhook_manager()
    webhook = manager.get(webhook_id)
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")
    return webhook.to_dict()


@router.put("/{webhook_id}")
async def update_webhook(
    webhook_id: str,
    request: UpdateWebhookRequest,
):
    """更新Webhook配置

    Args:
        webhook_id: Webhook ID
        request: 更新内容

    Returns:
        更新后的Webhook
    """
    manager = get_webhook_manager()
    webhook = manager.get(webhook_id)
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")

    # 验证事件类型
    if request.events:
        for event in request.events:
            try:
                WebhookEvent(event)
            except ValueError:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid event type: {event}",
                )

    # 更新
    manager._webhooks[webhook_id] = Webhook(
        id=webhook_id,
        url=request.url or webhook.url,
        events=request.events or webhook.events,
        secret=request.secret or webhook.secret,
        active=request.active if request.active is not None else webhook.active,
        created_at=webhook.created_at,
        last_triggered=webhook.last_triggered,
        failure_count=webhook.failure_count,
        last_error=webhook.last_error,
    )
    manager._save()

    return manager.get(webhook_id).to_dict()


@router.delete("/{webhook_id}")
def remove_webhook(webhook_id: str):
    """删除Webhook

    Args:
        webhook_id: Webhook ID

    Returns:
        操作结果
    """
    manager = get_webhook_manager()
    if not manager.remove(webhook_id):
        raise HTTPException(status_code=404, detail="Webhook not found")
    return {"status": "removed", "webhook_id": webhook_id}


@router.post("/{webhook_id}/test")
async def test_webhook(webhook_id: str):
    """测试Webhook

    Args:
        webhook_id: Webhook ID

    Returns:
        测试结果
    """
    manager = get_webhook_manager()
    webhook = manager.get(webhook_id)
    if not webhook:
        raise HTTPException(status_code=404, detail="Webhook not found")

    try:
        await manager._send_webhook(
            webhook,
            WebhookEvent.RESEARCH_COMPLETED,
            {
                "test": True,
                "message": "This is a test webhook trigger",
            },
        )
        return {"status": "success", "webhook_id": webhook_id}
    except Exception as e:
        return {"status": "failed", "webhook_id": webhook_id, "error": str(e)}
