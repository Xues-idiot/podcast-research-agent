"""书签系统 - 收藏特定时间点和内容"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Bookmark:
    """书签"""
    id: str = ""
    research_id: str = ""
    entry_id: str = ""  # 对应的文本段落ID
    timestamp: float = 0.0  # 时间戳（秒）
    formatted_time: str = ""  # 格式化时间
    content: str = ""  # 书签内容/笔记
    note: str = ""  # 用户笔记
    color: str = "#3498DB"  # 书签颜色
    created_at: str = ""

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(
                f"{self.research_id}:{self.timestamp}".encode()
            ).hexdigest()[:8]
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "research_id": self.research_id,
            "entry_id": self.entry_id,
            "timestamp": self.timestamp,
            "formatted_time": self.formatted_time,
            "content": self.content,
            "note": self.note,
            "color": self.color,
            "created_at": self.created_at,
        }


class BookmarkManager:
    """书签管理器"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化书签管理器"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "bookmarks"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._bookmarks_file = self.storage_path / "bookmarks.json"
        self._bookmarks: dict[str, Bookmark] = {}
        self._load()

    def _load(self):
        """加载书签数据"""
        if self._bookmarks_file.exists():
            try:
                with open(self._bookmarks_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for bm_data in data.values():
                        self._bookmarks[bm_data["id"]] = Bookmark(**bm_data)
            except (json.JSONDecodeError, KeyError):
                self._bookmarks = {}

    def _save(self):
        """保存书签数据"""
        data = {bid: bm.to_dict() for bid, bm in self._bookmarks.items()}
        temp_file = self._bookmarks_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._bookmarks_file)

    def add(
        self,
        research_id: str,
        timestamp: float,
        content: str = "",
        entry_id: str = "",
        note: str = "",
        color: str = "#3498DB",
    ) -> Bookmark:
        """添加书签

        Args:
            research_id: 研究ID
            timestamp: 时间戳
            content: 书签内容
            entry_id: 关联的文本段落ID
            note: 用户笔记
            color: 颜色

        Returns:
            书签
        """
        bookmark = Bookmark(
            research_id=research_id,
            entry_id=entry_id,
            timestamp=timestamp,
            formatted_time=self._format_timestamp(timestamp),
            content=content,
            note=note,
            color=color,
        )
        self._bookmarks[bookmark.id] = bookmark
        self._save()
        return bookmark

    def _format_timestamp(self, seconds: float) -> str:
        """格式化时间戳"""
        if seconds < 0:
            return "00:00"
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        return f"{minutes:02d}:{secs:02d}"

    def remove(self, bookmark_id: str) -> bool:
        """移除书签"""
        if bookmark_id in self._bookmarks:
            del self._bookmarks[bookmark_id]
            self._save()
            return True
        return False

    def get(self, bookmark_id: str) -> Optional[Bookmark]:
        """获取书签"""
        return self._bookmarks.get(bookmark_id)

    def list_by_research(self, research_id: str) -> list[Bookmark]:
        """列出某个研究的书签"""
        bookmarks = [
            bm for bm in self._bookmarks.values()
            if bm.research_id == research_id
        ]
        return sorted(bookmarks, key=lambda x: x.timestamp)

    def list_all(self, limit: int = 100) -> list[Bookmark]:
        """列出所有书签"""
        bookmarks = sorted(
            self._bookmarks.values(),
            key=lambda x: x.created_at,
            reverse=True
        )
        return bookmarks[:limit]

    def update_note(self, bookmark_id: str, note: str) -> bool:
        """更新笔记"""
        bookmark = self._bookmarks.get(bookmark_id)
        if bookmark:
            bookmark.note = note
            self._save()
            return True
        return False

    def update_color(self, bookmark_id: str, color: str) -> bool:
        """更新颜色"""
        bookmark = self._bookmarks.get(bookmark_id)
        if bookmark:
            bookmark.color = color
            self._save()
            return True
        return False

    def search(self, query: str) -> list[Bookmark]:
        """搜索书签"""
        query_lower = query.lower()
        results = []
        for bookmark in self._bookmarks.values():
            if (query_lower in bookmark.content.lower() or
                query_lower in bookmark.note.lower()):
                results.append(bookmark)
        return sorted(results, key=lambda x: x.created_at, reverse=True)

    def get_stats(self) -> dict:
        """获取书签统计"""
        return {
            "total": len(self._bookmarks),
            "by_research": len(set(bm.research_id for bm in self._bookmarks.values())),
        }


# 全局实例
_bookmark_manager: Optional[BookmarkManager] = None


def get_bookmark_manager() -> BookmarkManager:
    """获取全局书签管理器"""
    global _bookmark_manager
    if _bookmark_manager is None:
        _bookmark_manager = BookmarkManager()
    return _bookmark_manager
