"""Entry 模型 - 播客内容的可检索单元

Entry 是播客转录的最小检索单元，支持：
- 文本内容
- 时间戳范围
- 向量嵌入
- 元数据
"""

import hashlib
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Entry:
    """播客内容的最小检索单元

    Attributes:
        id: 唯一标识符
        podcast_id: 播客/视频ID
        raw: 原始转录文本
        compiled: 编译后的文本（用于检索）
        start_time: 开始时间戳（秒）
        end_time: 结束时间戳（秒）
        created_at: 创建时间
        metadata: 附加元数据
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    podcast_id: str = ""
    raw: str = ""
    compiled: str = ""
    start_time: float = 0.0
    end_time: float = 0.0
    created_at: datetime = field(default_factory=datetime.now)
    metadata: dict = field(default_factory=dict)

    def __post_init__(self):
        """确保compiled有默认值"""
        if not self.compiled:
            self.compiled = self.raw[:500] if self.raw else ""

    @property
    def duration(self) -> float:
        """获取该Entry的时长（秒）"""
        return self.end_time - self.start_time

    @property
    def hashed_id(self) -> str:
        """生成基于内容的哈希ID"""
        return hashlib.md5(self.raw.encode()).hexdigest()[:12]

    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "id": self.id,
            "podcast_id": self.podcast_id,
            "raw": self.raw,
            "compiled": self.compiled,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "created_at": self.created_at.isoformat(),
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Entry":
        """从字典创建"""
        data = data.copy()
        if "created_at" in data and isinstance(data["created_at"], str):
            data["created_at"] = datetime.fromisoformat(data["created_at"])
        return cls(**data)


class EntryStore:
    """Entry 存储管理器

    负责：
    - Entry 的持久化存储
    - 基于时间戳的检索
    - 向量相似度检索（待集成）
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化存储

        Args:
            storage_path: 存储路径，默认为 ~/.echo/knowledge/
        """
        from pathlib import Path

        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "knowledge"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._entries: dict[str, list[Entry]] = {}  # podcast_id -> entries

    def add_entries(self, podcast_id: str, entries: list[Entry]) -> int:
        """添加Entry到存储

        Args:
            podcast_id: 播客ID
            entries: Entry列表

        Returns:
            添加的Entry数量
        """
        if podcast_id not in self._entries:
            self._entries[podcast_id] = []

        self._entries[podcast_id].extend(entries)
        self._save(podcast_id)
        return len(entries)

    def get_entries(self, podcast_id: str) -> list[Entry]:
        """获取播客的所有Entry"""
        if podcast_id not in self._entries:
            self._load(podcast_id)
        return self._entries.get(podcast_id, [])

    def get_entries_by_time_range(
        self, podcast_id: str, start: float, end: float
    ) -> list[Entry]:
        """获取指定时间范围内的Entry

        Args:
            podcast_id: 播客ID
            start: 开始时间（秒）
            end: 结束时间（秒）

        Returns:
            时间范围内的Entry列表
        """
        entries = self.get_entries(podcast_id)
        return [
            e for e in entries
            if e.start_time < end and e.end_time > start
        ]

    def get_entry_by_id(self, podcast_id: str, entry_id: str) -> Optional[Entry]:
        """根据ID获取Entry"""
        entries = self.get_entries(podcast_id)
        for entry in entries:
            if entry.id == entry_id:
                return entry
        return None

    def delete_entries(self, podcast_id: str) -> int:
        """删除播客的所有Entry

        Returns:
            删除的Entry数量
        """
        if podcast_id in self._entries:
            count = len(self._entries[podcast_id])
            del self._entries[podcast_id]
            self._delete_file(podcast_id)
            return count
        return 0

    def search(
        self,
        podcast_id: str,
        query: str,
        top_k: int = 5,
    ) -> list[Entry]:
        """简单关键词搜索

        TODO: 集成向量检索

        Args:
            podcast_id: 播客ID
            query: 搜索查询
            top_k: 返回数量

        Returns:
            匹配的Entry列表
        """
        entries = self.get_entries(podcast_id)
        query_lower = query.lower()

        # 简单关键词匹配
        scored = []
        for entry in entries:
            score = 0
            if query_lower in entry.compiled.lower():
                score += 2
            if query_lower in entry.raw.lower():
                score += 1
            if score > 0:
                scored.append((score, entry))

        # 按分数排序
        scored.sort(key=lambda x: x[0], reverse=True)
        return [entry for _, entry in scored[:top_k]]

    def _save(self, podcast_id: str):
        """保存到文件"""
        import json

        file_path = self.storage_path / f"{podcast_id}.json"
        entries = self._entries.get(podcast_id, [])

        data = {
            "podcast_id": podcast_id,
            "entries": [e.to_dict() for e in entries],
            "updated_at": datetime.now().isoformat(),
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _load(self, podcast_id: str):
        """从文件加载"""
        import json

        file_path = self.storage_path / f"{podcast_id}.json"
        if not file_path.exists():
            self._entries[podcast_id] = []
            return

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self._entries[podcast_id] = [
                Entry.from_dict(e) for e in data.get("entries", [])
            ]
        except (json.JSONDecodeError, KeyError):
            self._entries[podcast_id] = []

    def _delete_file(self, podcast_id: str):
        """删除文件"""
        import os

        file_path = self.storage_path / f"{podcast_id}.json"
        if file_path.exists():
            os.remove(file_path)

    def list_podcasts(self) -> list[str]:
        """列出所有存储的播客ID"""
        files = self.storage_path.glob("*.json")
        return [f.stem for f in files if f.is_file()]
