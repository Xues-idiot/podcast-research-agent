"""研究统计分析 - 跟踪和分析使用数据"""

import json
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


@dataclass
class UsageStats:
    """使用统计"""
    total_researches: int = 0
    total_sources: dict = field(default_factory=lambda: defaultdict(int))  # source -> count
    total_duration_minutes: float = 0.0
    average_duration_minutes: float = 0.0
    total_keypoints: int = 0
    total_citations: int = 0
    platform_breakdown: dict = field(default_factory=lambda: defaultdict(int))
    daily_counts: dict = field(default_factory=dict)  # date -> count
    top_sources: list = field(default_factory=list)  # [(source, count), ...]

    def to_dict(self) -> dict:
        return {
            "total_researches": self.total_researches,
            "total_sources": dict(self.total_sources),
            "total_duration_minutes": self.total_duration_minutes,
            "average_duration_minutes": self.average_duration_minutes,
            "total_keypoints": self.total_keypoints,
            "total_citations": self.total_citations,
            "platform_breakdown": dict(self.platform_breakdown),
            "daily_counts": self.daily_counts,
            "top_sources": self.top_sources,
        }


@dataclass
class ResearchEvent:
    """研究事件"""
    id: str = ""
    research_id: str = ""
    event_type: str = ""  # created, completed, failed, exported
    source: str = ""
    platform: str = ""
    duration_seconds: float = 0.0
    keypoints_count: int = 0
    timestamp: str = ""

    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()


class AnalyticsManager:
    """分析管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化分析管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "analytics"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._events_file = self.storage_path / "events.json"
        self._events: list[ResearchEvent] = []
        self._load()

    def _load(self):
        """加载事件数据"""
        if self._events_file.exists():
            try:
                with open(self._events_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self._events = [ResearchEvent(**e) for e in data]
            except (json.JSONDecodeError, KeyError):
                self._events = []

    def _save(self):
        """保存事件数据"""
        data = [e.__dict__ for e in self._events]
        temp_file = self._events_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._events_file)

    def track(
        self,
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
        """
        event = ResearchEvent(
            research_id=research_id,
            event_type=event_type,
            source=source,
            platform=platform,
            duration_seconds=duration_seconds,
            keypoints_count=keypoints_count,
        )
        self._events.append(event)
        self._save()

    def track_completed(
        self,
        research_id: str,
        source: str = "",
        platform: str = "",
        duration_seconds: float = 0.0,
        keypoints_count: int = 0,
    ):
        """跟踪研究完成"""
        self.track(
            research_id=research_id,
            event_type="completed",
            source=source,
            platform=platform,
            duration_seconds=duration_seconds,
            keypoints_count=keypoints_count,
        )

    def get_stats(self, days: int = 30) -> UsageStats:
        """获取使用统计

        Args:
            days: 统计天数

        Returns:
            使用统计
        """
        cutoff = datetime.now() - timedelta(days=days)
        recent_events = [
            e for e in self._events
            if datetime.fromisoformat(e.timestamp) >= cutoff and e.event_type == "completed"
        ]

        stats = UsageStats()
        stats.total_researches = len(recent_events)

        # 来源统计
        for event in recent_events:
            if event.source:
                stats.total_sources[event.source] += 1
            if event.platform:
                stats.platform_breakdown[event.platform] += 1

        # 时长统计
        if recent_events:
            total_duration = sum(e.duration_seconds for e in recent_events)
            stats.total_duration_minutes = total_duration / 60.0
            stats.average_duration_minutes = stats.total_duration_minutes / len(recent_events)

        # 要点统计
        stats.total_keypoints = sum(e.keypoints_count for e in recent_events)

        # 每日统计
        for event in recent_events:
            date = event.timestamp[:10]
            stats.daily_counts[date] = stats.daily_counts.get(date, 0) + 1

        # Top来源
        stats.top_sources = sorted(
            stats.total_sources.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]

        return stats

    def get_daily_stats(self, days: int = 7) -> list[dict]:
        """获取每日统计

        Args:
            days: 天数

        Returns:
            每日统计数据
        """
        cutoff = datetime.now() - timedelta(days=days)
        recent_events = [
            e for e in self._events
            if datetime.fromisoformat(e.timestamp) >= cutoff
        ]

        daily_data = defaultdict(lambda: {
            "count": 0,
            "duration": 0.0,
            "keypoints": 0,
            "platforms": defaultdict(int),
        })

        for event in recent_events:
            date = event.timestamp[:10]
            daily_data[date]["count"] += 1
            if event.event_type == "completed":
                daily_data[date]["duration"] += event.duration_seconds / 60.0
                daily_data[date]["keypoints"] += event.keypoints_count
            if event.platform:
                daily_data[date]["platforms"][event.platform] += 1

        result = []
        for date in sorted(daily_data.keys()):
            data = daily_data[date]
            result.append({
                "date": date,
                "researches": data["count"],
                "duration_minutes": round(data["duration"], 1),
                "keypoints": data["keypoints"],
                "platforms": dict(data["platforms"]),
            })

        return result

    def get_platform_stats(self) -> dict:
        """获取平台统计"""
        events = [e for e in self._events if e.event_type == "completed"]
        platforms = defaultdict(lambda: {
            "count": 0,
            "total_duration": 0.0,
            "avg_duration": 0.0,
        })

        for event in events:
            if event.platform:
                platforms[event.platform]["count"] += 1
                platforms[event.platform]["total_duration"] += event.duration_seconds / 60.0

        for platform, data in platforms.items():
            if data["count"] > 0:
                data["avg_duration"] = data["total_duration"] / data["count"]

        return {k: dict(v) for k, v in platforms.items()}

    def get_recent_activity(self, limit: int = 20) -> list[dict]:
        """获取最近活动

        Args:
            limit: 返回数量

        Returns:
            最近活动列表
        """
        recent = sorted(
            self._events,
            key=lambda e: e.timestamp,
            reverse=True
        )[:limit]

        return [
            {
                "research_id": e.research_id,
                "event_type": e.event_type,
                "source": e.source,
                "platform": e.platform,
                "timestamp": e.timestamp,
            }
            for e in recent
        ]

    def get_streak(self) -> dict:
        """获取连续活跃天数"""
        if not self._events:
            return {"current_streak": 0, "longest_streak": 0, "last_active": None}

        completed_events = [
            e for e in self._events
            if e.event_type == "completed"
        ]
        if not completed_events:
            return {"current_streak": 0, "longest_streak": 0, "last_active": None}

        # 获取所有活跃日期
        active_dates = set(e.timestamp[:10] for e in completed_events)
        sorted_dates = sorted(active_dates, reverse=True)

        last_active = sorted_dates[0]

        # 计算当前连续天数
        current_streak = 0
        today = datetime.now().date()
        check_date = today

        while True:
            date_str = check_date.isoformat()
            if date_str in active_dates:
                current_streak += 1
                check_date -= timedelta(days=1)
            else:
                break

        # 计算最长连续天数
        longest_streak = 0
        streak = 0
        prev_date = None

        for date_str in sorted(active_dates):
            date = datetime.fromisoformat(date_str).date()
            if prev_date is None or (prev_date - date).days == 1:
                streak += 1
            else:
                streak = 1
            longest_streak = max(longest_streak, streak)
            prev_date = date

        return {
            "current_streak": current_streak,
            "longest_streak": longest_streak,
            "last_active": last_active,
        }

    def clear_old_events(self, days: int = 90):
        """清理旧事件"""
        cutoff = datetime.now() - timedelta(days=days)
        old_count = len(self._events)
        self._events = [
            e for e in self._events
            if datetime.fromisoformat(e.timestamp) >= cutoff
        ]
        if len(self._events) < old_count:
            self._save()
        return old_count - len(self._events)


# 全局实例
_analytics_manager: Optional[AnalyticsManager] = None


def get_analytics_manager() -> AnalyticsManager:
    """获取全局分析管理器"""
    global _analytics_manager
    if _analytics_manager is None:
        _analytics_manager = AnalyticsManager()
    return _analytics_manager
