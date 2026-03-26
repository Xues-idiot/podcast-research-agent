"""播客订阅系统 - 管理播客订阅和自动更新"""

import asyncio
import hashlib
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Optional
import json


class SubscriptionStatus(Enum):
    """订阅状态"""
    ACTIVE = "active"
    PAUSED = "paused"
    ERROR = "error"


@dataclass
class Subscription:
    """播客订阅"""
    id: str = ""
    url: str = ""
    title: str = ""
    feed_url: str = ""
    platform: str = ""
    status: SubscriptionStatus = SubscriptionStatus.ACTIVE
    last_check: str = ""
    last_update: str = ""
    update_interval_hours: int = 24  # 检查间隔（小时）
    auto_research: bool = False  # 是否自动研究新剧集
    created_at: str = ""
    error_count: int = 0
    last_error: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(self.url.encode()).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


@dataclass
class Episode:
    """剧集"""
    id: str
    subscription_id: str
    title: str
    url: str
    published_at: str = ""
    duration: int = 0
    is_new: bool = True  # 是否为新剧集
    research_status: str = ""  # pending, researching, completed, failed


class SubscriptionManager:
    """订阅管理器

    管理播客订阅，支持：
    - 添加/移除订阅
    - 定期检查更新
    - 自动研究新剧集
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化订阅管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "subscriptions"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._subscriptions_file = self.storage_path / "subscriptions.json"
        self._episodes_file = self.storage_path / "episodes.json"
        self._subscriptions: dict[str, Subscription] = {}
        self._episodes: dict[str, list[Episode]] = {}
        self._load()

    def _load(self):
        """加载订阅数据"""
        # 加载订阅
        if self._subscriptions_file.exists():
            try:
                with open(self._subscriptions_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                for sub_data in data.values():
                    sub_data["status"] = SubscriptionStatus(sub_data.get("status", "active"))
                    self._subscriptions[sub_data["id"]] = Subscription(**sub_data)
            except (json.JSONDecodeError, KeyError, ValueError):
                self._subscriptions = {}

        # 加载剧集
        if self._episodes_file.exists():
            try:
                with open(self._episodes_file, "r", encoding="utf-8") as f:
                    self._episodes = json.load(f)
            except json.JSONDecodeError:
                self._episodes = {}

    def _save(self):
        """保存订阅数据"""
        # 保存订阅
        data = {
            sub_id: {
                **sub.to_dict(),
                "status": sub.status.value,
            }
            for sub_id, sub in self._subscriptions.items()
        }
        temp_file = self._subscriptions_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._subscriptions_file)

        # 保存剧集
        temp_file = self._episodes_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._episodes, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._episodes_file)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "feed_url": self.feed_url,
            "platform": self.platform,
            "status": self.status.value,
            "last_check": self.last_check,
            "last_update": self.last_update,
            "update_interval_hours": self.update_interval_hours,
            "auto_research": self.auto_research,
            "created_at": self.created_at,
            "error_count": self.error_count,
            "last_error": self.last_error,
        }

    def add(
        self,
        url: str,
        title: str = "",
        feed_url: str = "",
        platform: str = "",
        update_interval_hours: int = 24,
        auto_research: bool = False,
    ) -> Subscription:
        """添加订阅"""
        sub = Subscription(
            url=url,
            title=title or url,
            feed_url=feed_url or url,
            platform=platform,
            update_interval_hours=update_interval_hours,
            auto_research=auto_research,
        )
        self._subscriptions[sub.id] = sub
        self._episodes[sub.id] = []
        self._save()
        return sub

    def remove(self, subscription_id: str) -> bool:
        """移除订阅"""
        if subscription_id in self._subscriptions:
            del self._subscriptions[subscription_id]
            if subscription_id in self._episodes:
                del self._episodes[subscription_id]
            self._save()
            return True
        return False

    def get(self, subscription_id: str) -> Optional[Subscription]:
        """获取订阅"""
        return self._subscriptions.get(subscription_id)

    def list(
        self,
        status: Optional[SubscriptionStatus] = None,
        platform: Optional[str] = None,
    ) -> list[Subscription]:
        """列出订阅"""
        results = list(self._subscriptions.values())

        if status:
            results = [s for s in results if s.status == status]

        if platform:
            results = [s for s in results if s.platform == platform]

        return results

    def update(self, subscription_id: str, **kwargs) -> bool:
        """更新订阅配置"""
        sub = self._subscriptions.get(subscription_id)
        if not sub:
            return False

        for key, value in kwargs.items():
            if hasattr(sub, key):
                setattr(sub, key, value)

        sub.last_check = datetime.now().isoformat()
        self._save()
        return True

    def check_updates(self, subscription_id: str) -> list[Episode]:
        """检查订阅更新"""
        sub = self._subscriptions.get(subscription_id)
        if not sub:
            return []

        sub.last_check = datetime.now().isoformat()

        # TODO: 实际实现RSS检查
        # 目前返回空列表，实际使用时需要集成RSS解析器
        new_episodes = []

        if new_episodes:
            sub.last_update = datetime.now().isoformat()
            sub.error_count = 0

        self._save()
        return new_episodes

    def get_episodes(self, subscription_id: str) -> list[Episode]:
        """获取订阅的所有剧集"""
        return [Episode(**e) for e in self._episodes.get(subscription_id, [])]

    def mark_episode_researched(self, subscription_id: str, episode_id: str, status: str):
        """标记剧集研究状态"""
        episodes = self._episodes.get(subscription_id, [])
        for ep in episodes:
            if ep.get("id") == episode_id:
                ep["research_status"] = status
                break
        self._save()


# 全局实例
_subscription_manager: Optional[SubscriptionManager] = None


def get_subscription_manager() -> SubscriptionManager:
    """获取全局订阅管理器"""
    global _subscription_manager
    if _subscription_manager is None:
        _subscription_manager = SubscriptionManager()
    return _subscription_manager
