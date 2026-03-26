"""研究历史记录 - 记录和管理研究历史"""

import json
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class ResearchHistoryEntry:
    """研究历史条目"""
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    url: str = ""
    title: str = ""
    podcast_id: str = ""
    platform: str = ""
    duration: int = 0  # 秒
    created_at: str = ""
    tags: list[str] = field(default_factory=list)
    notes: str = ""
    favorite: bool = False

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchHistoryEntry":
        return cls(**data)


class ResearchHistory:
    """研究历史管理器

    管理播客研究历史记录，支持：
    - 添加研究记录
    - 按标签筛选
    - 收藏夹功能
    - 搜索历史
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化历史管理器

        Args:
            storage_path: 存储路径，默认为 ~/.echo/history/
        """
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "history"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._history_file = self.storage_path / "history.json"
        self._entries: dict[str, ResearchHistoryEntry] = {}
        self._load()

    def _load(self):
        """从文件加载历史"""
        if not self._history_file.exists():
            return

        try:
            with open(self._history_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for entry_data in data.values():
                entry = ResearchHistoryEntry.from_dict(entry_data)
                self._entries[entry.id] = entry
        except (json.JSONDecodeError, KeyError):
            self._entries = {}

    def _save(self):
        """保存历史到文件"""
        data = {
            entry_id: entry.to_dict()
            for entry_id, entry in self._entries.items()
        }

        # 原子性写入
        temp_file = self._history_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._history_file)

    def add(
        self,
        url: str,
        title: str = "",
        podcast_id: str = "",
        platform: str = "",
        duration: int = 0,
    ) -> ResearchHistoryEntry:
        """添加研究记录

        Args:
            url: 播客URL
            title: 标题
            podcast_id: 播客ID
            platform: 平台
            duration: 时长（秒）

        Returns:
            创建的历史条目
        """
        entry = ResearchHistoryEntry(
            url=url,
            title=title,
            podcast_id=podcast_id,
            platform=platform,
            duration=duration,
        )
        self._entries[entry.id] = entry
        self._save()
        return entry

    def get(self, entry_id: str) -> Optional[ResearchHistoryEntry]:
        """获取历史条目"""
        return self._entries.get(entry_id)

    def list(
        self,
        platform: Optional[str] = None,
        tag: Optional[str] = None,
        favorite: Optional[bool] = None,
        search: Optional[str] = None,
        limit: int = 50,
    ) -> list[ResearchHistoryEntry]:
        """列出历史条目

        Args:
            platform: 按平台筛选
            tag: 按标签筛选
            favorite: 按收藏筛选
            search: 搜索关键词
            limit: 返回数量限制

        Returns:
            历史条目列表
        """
        results = list(self._entries.values())

        # 按平台筛选
        if platform:
            results = [e for e in results if e.platform == platform]

        # 按标签筛选
        if tag:
            results = [e for e in results if tag in e.tags]

        # 按收藏筛选
        if favorite is not None:
            results = [e for e in results if e.favorite == favorite]

        # 搜索
        if search:
            search_lower = search.lower()
            results = [
                e for e in results
                if search_lower in e.title.lower()
                or search_lower in e.url.lower()
                or search_lower in e.platform.lower()
            ]

        # 按时间排序（最新的在前）
        results.sort(key=lambda e: e.created_at, reverse=True)

        return results[:limit]

    def add_tag(self, entry_id: str, tag: str) -> bool:
        """添加标签

        Args:
            entry_id: 条目ID
            tag: 标签

        Returns:
            是否成功
        """
        entry = self._entries.get(entry_id)
        if not entry:
            return False

        if tag not in entry.tags:
            entry.tags.append(tag)
            self._save()
        return True

    def remove_tag(self, entry_id: str, tag: str) -> bool:
        """移除标签"""
        entry = self._entries.get(entry_id)
        if not entry:
            return False

        if tag in entry.tags:
            entry.tags.remove(tag)
            self._save()
        return True

    def toggle_favorite(self, entry_id: str) -> bool:
        """切换收藏状态"""
        entry = self._entries.get(entry_id)
        if not entry:
            return False

        entry.favorite = not entry.favorite
        self._save()
        return True

    def update_notes(self, entry_id: str, notes: str) -> bool:
        """更新笔记"""
        entry = self._entries.get(entry_id)
        if not entry:
            return False

        entry.notes = notes
        self._save()
        return True

    def delete(self, entry_id: str) -> bool:
        """删除历史条目"""
        if entry_id in self._entries:
            del self._entries[entry_id]
            self._save()
            return True
        return False

    def clear(self):
        """清空所有历史"""
        self._entries.clear()
        self._save()

    def get_stats(self) -> dict:
        """获取统计信息"""
        entries = list(self._entries.values())
        platforms = {}
        total_tags = {}
        favorites = sum(1 for e in entries if e.favorite)

        for entry in entries:
            # 平台统计
            if entry.platform:
                platforms[entry.platform] = platforms.get(entry.platform, 0) + 1

            # 标签统计
            for tag in entry.tags:
                total_tags[tag] = total_tags.get(tag, 0) + 1

        # 获取最常用的标签
        top_tags = sorted(total_tags.items(), key=lambda x: x[1], reverse=True)[:10]

        return {
            "total": len(entries),
            "favorites": favorites,
            "platforms": platforms,
            "top_tags": top_tags,
        }


# 全局实例
_history: Optional[ResearchHistory] = None


def get_research_history() -> ResearchHistory:
    """获取全局研究历史实例"""
    global _history
    if _history is None:
        _history = ResearchHistory()
    return _history
