"""通知提醒系统 - 研究完成、新剧集等提醒"""

import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Optional


class NotificationType(Enum):
    """通知类型"""
    RESEARCH_COMPLETED = "research_completed"
    NEW_EPISODE = "new_episode"
    SUBSCRIPTION_UPDATE = "subscription_update"
    SHARE_ACCESSED = "share_accessed"
    WEEKLY_SUMMARY = "weekly_summary"
    SYSTEM = "system"


class NotificationPriority(Enum):
    """通知优先级"""
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"


@dataclass
class Notification:
    """通知"""
    id: str = ""
    type: NotificationType = NotificationType.SYSTEM
    title: str = ""
    message: str = ""
    priority: NotificationPriority = NotificationPriority.NORMAL
    data: dict = field(default_factory=dict)  # 额外数据
    read: bool = False
    dismissed: bool = False
    created_at: str = ""
    expires_at: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = f"notif_{datetime.now().timestamp()}"
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class NotificationManager:
    """通知管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化通知管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "notifications"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._notifications_file = self.storage_path / "notifications.json"
        self._settings_file = self.storage_path / "settings.json"
        self._notifications: list[Notification] = []
        self._settings: dict = self._default_settings()
        self._load()

    def _default_settings(self) -> dict:
        """默认设置"""
        return {
            "enabled": True,
            "research_completed": True,
            "new_episode": True,
            "subscription_update": True,
            "share_accessed": False,
            "weekly_summary": True,
            "quiet_hours_start": "",  # 如 "22:00"
            "quiet_hours_end": "",    # 如 "08:00"
            "max_notifications": 100,
        }

    def _load(self):
        """加载通知数据"""
        if self._notifications_file.exists():
            try:
                with open(self._notifications_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for notif_data in data:
                        notif_data["type"] = NotificationType(notif_data["type"])
                        notif_data["priority"] = NotificationPriority(notif_data["priority"])
                        self._notifications.append(Notification(**notif_data))
            except (json.JSONDecodeError, KeyError, ValueError):
                self._notifications = []

        if self._settings_file.exists():
            try:
                with open(self._settings_file, "r", encoding="utf-8") as f:
                    self._settings = {**self._default_settings(), **json.load(f)}
            except json.JSONDecodeError:
                self._settings = self._default_settings()

    def _save(self):
        """保存通知数据"""
        data = [n.__dict__ for n in self._notifications]
        temp_file = self._notifications_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._notifications_file)

        temp_file = self._settings_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(self._settings, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._settings_file)

    def _is_quiet_hours(self) -> bool:
        """检查是否在安静时段"""
        if not self._settings.get("quiet_hours_start") or not self._settings.get("quiet_hours_end"):
            return False

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        start = self._settings["quiet_hours_start"]
        end = self._settings["quiet_hours_end"]

        if start <= end:
            return start <= current_time <= end
        else:
            return current_time >= start or current_time <= end

    def _should_notify(self, notif_type: NotificationType) -> bool:
        """检查是否应该发送通知"""
        if not self._settings.get("enabled"):
            return False

        type_map = {
            NotificationType.RESEARCH_COMPLETED: "research_completed",
            NotificationType.NEW_EPISODE: "new_episode",
            NotificationType.SUBSCRIPTION_UPDATE: "subscription_update",
            NotificationType.SHARE_ACCESSED: "share_accessed",
            NotificationType.WEEKLY_SUMMARY: "weekly_summary",
        }

        setting_key = type_map.get(notif_type)
        if not setting_key:
            return True

        return self._settings.get(setting_key, True)

    def send(
        self,
        notif_type: NotificationType,
        title: str,
        message: str,
        priority: NotificationPriority = NotificationPriority.NORMAL,
        data: dict = None,
        skip_quiet_hours: bool = False,
    ) -> Optional[Notification]:
        """发送通知

        Args:
            notif_type: 通知类型
            title: 标题
            message: 消息
            priority: 优先级
            data: 额外数据
            skip_quiet_hours: 跳过安静时段检查

        Returns:
            通知对象
        """
        if not self._should_notify(notif_type):
            return None

        if not skip_quiet_hours and self._is_quiet_hours():
            # 延迟到安静时段结束后
            pass

        notification = Notification(
            type=notif_type,
            title=title,
            message=message,
            priority=priority,
            data=data or {},
        )

        self._notifications.insert(0, notification)

        # 限制通知数量
        max_notif = self._settings.get("max_notifications", 100)
        if len(self._notifications) > max_notif:
            self._notifications = self._notifications[:max_notif]

        self._save()
        return notification

    def send_research_completed(
        self,
        research_id: str,
        title: str,
        source: str,
    ) -> Optional[Notification]:
        """发送研究完成通知"""
        return self.send(
            notif_type=NotificationType.RESEARCH_COMPLETED,
            title=f"研究完成: {title[:30]}",
            message=f"来自 {source} 的播客研究已完成",
            data={"research_id": research_id, "source": source},
        )

    def send_new_episode(
        self,
        subscription_id: str,
        subscription_title: str,
        episode_title: str,
    ) -> Optional[Notification]:
        """发送新剧集通知"""
        return self.send(
            notif_type=NotificationType.NEW_EPISODE,
            title=f"新剧集: {subscription_title[:20]}",
            message=episode_title[:50],
            data={"subscription_id": subscription_id, "episode_title": episode_title},
        )

    def send_share_accessed(
        self,
        share_id: str,
        share_token: str,
    ) -> Optional[Notification]:
        """发送分享被访问通知"""
        return self.send(
            notif_type=NotificationType.SHARE_ACCESSED,
            title="分享被访问",
            message="有人查看了你的研究分享",
            priority=NotificationPriority.LOW,
            data={"share_id": share_id},
        )

    def list(
        self,
        unread_only: bool = False,
        notif_type: Optional[NotificationType] = None,
        limit: int = 50,
    ) -> list[Notification]:
        """列出通知"""
        results = self._notifications

        if unread_only:
            results = [n for n in results if not n.read]

        if notif_type:
            results = [n for n in results if n.type == notif_type]

        # 清理过期通知
        now = datetime.now()
        results = [
            n for n in results
            if not n.expires_at or datetime.fromisoformat(n.expires_at) > now
        ]

        return results[:limit]

    def mark_read(self, notification_id: str) -> bool:
        """标记已读"""
        for notif in self._notifications:
            if notif.id == notification_id:
                notif.read = True
                self._save()
                return True
        return False

    def mark_all_read(self) -> int:
        """标记所有已读"""
        count = 0
        for notif in self._notifications:
            if not notif.read:
                notif.read = True
                count += 1
        if count > 0:
            self._save()
        return count

    def dismiss(self, notification_id: str) -> bool:
        """关闭通知"""
        for notif in self._notifications:
            if notif.id == notification_id:
                notif.dismissed = True
                self._save()
                return True
        return False

    def delete(self, notification_id: str) -> bool:
        """删除通知"""
        for i, notif in enumerate(self._notifications):
            if notif.id == notification_id:
                del self._notifications[i]
                self._save()
                return True
        return False

    def clear_all(self):
        """清除所有通知"""
        self._notifications = []
        self._save()

    def get_unread_count(self) -> int:
        """获取未读数量"""
        return sum(1 for n in self._notifications if not n.read and not n.dismissed)

    def get_settings(self) -> dict:
        """获取设置"""
        return self._settings.copy()

    def update_settings(self, settings: dict) -> dict:
        """更新设置"""
        self._settings = {**self._settings, **settings}
        self._save()
        return self._settings

    def get_weekly_summary(self) -> dict:
        """生成周报"""
        now = datetime.now()
        week_ago = now - timedelta(days=7)

        recent = [
            n for n in self._notifications
            if datetime.fromisoformat(n.created_at) >= week_ago
        ]

        return {
            "period": f"{week_ago.date()} 至 {now.date()}",
            "total_notifications": len(recent),
            "by_type": {
                nt.value: sum(1 for n in recent if n.type == nt)
                for nt in NotificationType
            },
            "unread": self.get_unread_count(),
        }


# 全局实例
_notification_manager: Optional[NotificationManager] = None


def get_notification_manager() -> NotificationManager:
    """获取全局通知管理器"""
    global _notification_manager
    if _notification_manager is None:
        _notification_manager = NotificationManager()
    return _notification_manager
