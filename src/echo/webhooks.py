"""Webhook通知系统 - 研究完成时发送通知"""

import asyncio
import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional
import httpx


class WebhookEvent(Enum):
    """Webhook事件类型"""
    RESEARCH_COMPLETED = "research.completed"
    RESEARCH_FAILED = "research.failed"
    SUBSCRIPTION_NEW_EPISODE = "subscription.new_episode"
    CACHE_CLEARED = "cache.cleared"


@dataclass
class Webhook:
    """Webhook配置"""
    id: str = ""
    url: str = ""
    secret: str = ""
    events: list[str] = field(default_factory=list)  # 事件类型列表
    active: bool = True
    created_at: str = ""
    last_triggered: str = ""
    failure_count: int = 0
    last_error: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(self.url.encode()).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "url": self.url,
            "secret": self.secret,
            "events": self.events,
            "active": self.active,
            "created_at": self.created_at,
            "last_triggered": self.last_triggered,
            "failure_count": self.failure_count,
            "last_error": self.last_error,
        }


class WebhookManager:
    """Webhook管理器

    管理Webhook配置和触发。
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化Webhook管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "webhooks"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._webhooks_file = self.storage_path / "webhooks.json"
        self._webhooks: dict[str, Webhook] = {}
        self._load()

    def _load(self):
        """加载Webhook数据"""
        if not self._webhooks_file.exists():
            return

        try:
            with open(self._webhooks_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            for wh_data in data.values():
                self._webhooks[wh_data["id"]] = Webhook(**wh_data)
        except (json.JSONDecodeError, KeyError):
            self._webhooks = {}

    def _save(self):
        """保存Webhook数据"""
        data = {wh_id: wh.to_dict() for wh_id, wh in self._webhooks.items()}
        temp_file = self._webhooks_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._webhooks_file)

    def add(
        self,
        url: str,
        events: list[str],
        secret: str = "",
    ) -> Webhook:
        """添加Webhook

        Args:
            url: Webhook URL
            events: 监听的事件类型
            secret: 签名密钥

        Returns:
            创建的Webhook
        """
        webhook = Webhook(
            url=url,
            events=events,
            secret=secret,
        )
        self._webhooks[webhook.id] = webhook
        self._save()
        return webhook

    def remove(self, webhook_id: str) -> bool:
        """移除Webhook"""
        if webhook_id in self._webhooks:
            del self._webhooks[webhook_id]
            self._save()
            return True
        return False

    def get(self, webhook_id: str) -> Optional[Webhook]:
        """获取Webhook"""
        return self._webhooks.get(webhook_id)

    def list(self, active_only: bool = False) -> list[Webhook]:
        """列出Webhooks"""
        webhooks = list(self._webhooks.values())
        if active_only:
            webhooks = [w for w in webhooks if w.active]
        return webhooks

    async def trigger(self, event: WebhookEvent, data: dict):
        """触发Webhook

        Args:
            event: 事件类型
            data: 事件数据
        """
        for webhook in self._webhooks.values():
            if not webhook.active:
                continue

            if event.value not in webhook.events:
                continue

            try:
                await self._send_webhook(webhook, event, data)
                webhook.last_triggered = datetime.now().isoformat()
                webhook.failure_count = 0
                webhook.last_error = ""
            except Exception as e:
                webhook.failure_count += 1
                webhook.last_error = str(e)

        self._save()

    async def _send_webhook(
        self,
        webhook: Webhook,
        event: WebhookEvent,
        data: dict,
    ):
        """发送Webhook请求"""
        import hmac
        import base64

        # 准备载荷
        payload = {
            "event": event.value,
            "timestamp": datetime.now().isoformat(),
            "data": data,
        }
        payload_json = json.dumps(payload, ensure_ascii=False)

        # 准备请求头
        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Event": event.value,
            "X-Webhook-Timestamp": payload_json,
        }

        # 如果有密钥，添加签名
        if webhook.secret:
            signature = hmac.new(
                webhook.secret.encode(),
                payload_json.encode(),
                hashlib.sha256,
            ).digest()
            headers["X-Webhook-Signature"] = base64.b64encode(signature).decode()

        # 发送请求
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                webhook.url,
                content=payload_json,
                headers=headers,
            )
            response.raise_for_status()


# 全局实例
_webhook_manager: Optional[WebhookManager] = None


def get_webhook_manager() -> WebhookManager:
    """获取全局Webhook管理器"""
    global _webhook_manager
    if _webhook_manager is None:
        _webhook_manager = WebhookManager()
    return _webhook_manager
