"""定时提醒系统 - 设置播客研究提醒"""

import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Optional


class ReminderType(Enum):
    """提醒类型"""
    ONCE = "once"  # 单次
    DAILY = "daily"  # 每天
    WEEKLY = "weekly"  # 每周
    CUSTOM = "custom"  # 自定义


class ReminderStatus(Enum):
    """提醒状态"""
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    EXPIRED = "expired"


@dataclass
class Reminder:
    """提醒"""
    id: str = ""
    title: str = ""
    message: str = ""
    reminder_type: ReminderType = ReminderType.ONCE
    scheduled_at: str = ""  # ISO格式时间
    repeat_interval_hours: int = 0  # 重复间隔
    status: ReminderStatus = ReminderStatus.ACTIVE
    created_at: str = ""
    last_triggered: str = ""


class ReminderScheduler:
    """提醒调度器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化调度器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "reminders"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._reminders_file = self.storage_path / "reminders.json"
        self._reminders: dict[str, Reminder] = {}
        self._load()

    def _load(self):
        """加载提醒数据"""
        if self._reminders_file.exists():
            try:
                with open(self._reminders_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for rid, r_data in data.items():
                        r_data["reminder_type"] = ReminderType(r_data.get("reminder_type", "once"))
                        r_data["status"] = ReminderStatus(r_data.get("status", "active"))
                        self._reminders[rid] = Reminder(**r_data)
            except (json.JSONDecodeError, ValueError):
                self._reminders = {}

    def _save(self):
        """保存提醒数据"""
        data = {
            rid: {
                **r.__dict__,
                "reminder_type": r.reminder_type.value,
                "status": r.status.value,
            }
            for rid, r in self._reminders.items()
        }
        temp_file = self._reminders_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._reminders_file)

    def create(
        self,
        title: str,
        message: str = "",
        reminder_type: ReminderType = ReminderType.ONCE,
        scheduled_at: str = "",
        repeat_interval_hours: int = 0,
    ) -> Reminder:
        """创建提醒

        Args:
            title: 标题
            message: 消息
            reminder_type: 提醒类型
            scheduled_at: 计划时间
            repeat_interval_hours: 重复间隔

        Returns:
            创建的提醒
        """
        reminder = Reminder(
            title=title,
            message=message,
            reminder_type=reminder_type,
            scheduled_at=scheduled_at or datetime.now().isoformat(),
            repeat_interval_hours=repeat_interval_hours,
        )
        self._reminders[reminder.id] = reminder
        self._save()
        return reminder

    def get_pending(self) -> list[Reminder]:
        """获取待触发提醒"""
        now = datetime.now()
        pending = []

        for reminder in self._reminders.values():
            if reminder.status != ReminderStatus.ACTIVE:
                continue

            try:
                scheduled = datetime.fromisoformat(reminder.scheduled_at)
                if scheduled <= now:
                    pending.append(reminder)
            except:
                pass

        return pending

    def trigger(self, reminder_id: str) -> bool:
        """触发提醒

        Args:
            reminder_id: 提醒ID

        Returns:
            是否成功
        """
        reminder = self._reminders.get(reminder_id)
        if not reminder:
            return False

        reminder.last_triggered = datetime.now().isoformat()

        # 根据类型处理
        if reminder.reminder_type == ReminderType.ONCE:
            reminder.status = ReminderStatus.COMPLETED
        elif reminder.reminder_type == ReminderType.DAILY:
            reminder.scheduled_at = (datetime.now() + timedelta(days=1)).isoformat()
        elif reminder.reminder_type == ReminderType.WEEKLY:
            reminder.scheduled_at = (datetime.now() + timedelta(weeks=1)).isoformat()
        elif reminder.reminder_type == ReminderType.CUSTOM:
            if reminder.repeat_interval_hours > 0:
                reminder.scheduled_at = (
                    datetime.now() + timedelta(hours=reminder.repeat_interval_hours)
                ).isoformat()

        self._save()
        return True

    def cancel(self, reminder_id: str) -> bool:
        """取消提醒"""
        if reminder_id in self._reminders:
            self._reminders[reminder_id].status = ReminderStatus.EXPIRED
            self._save()
            return True
        return False

    def pause(self, reminder_id: str) -> bool:
        """暂停提醒"""
        if reminder_id in self._reminders:
            self._reminders[reminder_id].status = ReminderStatus.PAUSED
            self._save()
            return True
        return False

    def resume(self, reminder_id: str) -> bool:
        """恢复提醒"""
        if reminder_id in self._reminders:
            self._reminders[reminder_id].status = ReminderStatus.ACTIVE
            self._save()
            return True
        return False

    def list_all(self) -> list[Reminder]:
        """列出所有提醒"""
        return list(self._reminders.values())


# 全局实例
_reminder_scheduler: Optional[ReminderScheduler] = None


def get_reminder_scheduler() -> ReminderScheduler:
    """获取全局提醒调度器"""
    global _reminder_scheduler
    if _reminder_scheduler is None:
        _reminder_scheduler = ReminderScheduler()
    return _reminder_scheduler
