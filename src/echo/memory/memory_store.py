"""记忆存储 - 用户记忆持久化管理

参考 deer-flow 的 memory.json 结构，
存储用户上下文、偏好和历史。
"""

import json
import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class Fact:
    """记忆事实"""
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    content: str = ""
    category: str = "context"  # preference, knowledge, context, behavior, goal
    confidence: float = 0.5
    created_at: str = ""
    source: str = ""

    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Fact":
        return cls(**data)


@dataclass
class UserMemory:
    """用户记忆

    Attributes:
        user_id: 用户标识
        work_context: 工作上下文
        personal_context: 个人上下文
        top_of_mind: 当前最关注的内容
        recent_months: 最近几个月的记忆
        earlier_context: 早期上下文
        long_term_background: 长期背景
        facts: 事实列表
        updated_at: 最后更新时间
    """
    user_id: str = "default"
    work_context: str = ""
    personal_context: str = ""
    top_of_mind: str = ""
    recent_months: str = ""
    earlier_context: str = ""
    long_term_background: str = ""
    facts: list[Fact] = field(default_factory=list)
    updated_at: str = ""

    def __post_init__(self):
        if not self.updated_at:
            self.updated_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "work_context": self.work_context,
            "personal_context": self.personal_context,
            "top_of_mind": self.top_of_mind,
            "recent_months": self.recent_months,
            "earlier_context": self.earlier_context,
            "long_term_background": self.long_term_background,
            "facts": [f.to_dict() if isinstance(f, Fact) else f for f in self.facts],
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "UserMemory":
        if "facts" in data:
            data["facts"] = [Fact.from_dict(f) if isinstance(f, dict) else f for f in data["facts"]]
        return cls(**data)


class MemoryStore:
    """记忆存储管理器

    负责：
    - 记忆的持久化存储
    - 基于用户的记忆管理
    - 记忆的加载和保存
    """

    def __init__(self, storage_path: Optional[str] = None):
        """初始化存储

        Args:
            storage_path: 存储路径，默认为 ~/.echo/memory/
        """
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "memory"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._memory_file = self.storage_path / "memory.json"
        self._memories: dict[str, UserMemory] = {}
        self._load()

    def _load(self):
        """从文件加载记忆"""
        if not self._memory_file.exists():
            return

        try:
            with open(self._memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for user_id, mem_data in data.items():
                self._memories[user_id] = UserMemory.from_dict(mem_data)
        except (json.JSONDecodeError, KeyError):
            self._memories = {}

    def _save(self):
        """保存记忆到文件"""
        data = {
            user_id: memory.to_dict()
            for user_id, memory in self._memories.items()
        }

        # 原子性写入：先写临时文件再重命名
        temp_file = self._memory_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._memory_file)

    def get_memory(self, user_id: str = "default") -> UserMemory:
        """获取用户记忆

        Args:
            user_id: 用户ID

        Returns:
            用户记忆对象
        """
        if user_id not in self._memories:
            self._memories[user_id] = UserMemory(user_id=user_id)
        return self._memories[user_id]

    def update_memory(self, user_id: str = "default", **kwargs) -> UserMemory:
        """更新用户记忆

        Args:
            user_id: 用户ID
            **kwargs: 要更新的字段

        Returns:
            更新后的用户记忆
        """
        memory = self.get_memory(user_id)

        for key, value in kwargs.items():
            if hasattr(memory, key):
                setattr(memory, key, value)

        memory.updated_at = datetime.now().isoformat()
        self._save()
        return memory

    def add_fact(
        self,
        user_id: str = "default",
        content: str = "",
        category: str = "context",
        confidence: float = 0.5,
        source: str = ""
    ) -> Fact:
        """添加记忆事实

        Args:
            user_id: 用户ID
            content: 事实内容
            category: 分类
            confidence: 置信度
            source: 来源

        Returns:
            添加的事实
        """
        fact = Fact(
            content=content,
            category=category,
            confidence=confidence,
            source=source,
        )

        memory = self.get_memory(user_id)
        memory.facts.append(fact)

        # 限制事实数量
        if len(memory.facts) > 100:
            memory.facts = sorted(memory.facts, key=lambda f: f.confidence, reverse=True)[:100]

        self._save()
        return fact

    def get_facts(
        self,
        user_id: str = "default",
        category: Optional[str] = None,
        min_confidence: float = 0.0
    ) -> list[Fact]:
        """获取记忆事实

        Args:
            user_id: 用户ID
            category: 过滤分类
            min_confidence: 最低置信度

        Returns:
            事实列表
        """
        memory = self.get_memory(user_id)
        facts = memory.facts

        if category:
            facts = [f for f in facts if f.category == category]

        if min_confidence > 0:
            facts = [f for f in facts if f.confidence >= min_confidence]

        return sorted(facts, key=lambda f: f.confidence, reverse=True)

    def get_recent_facts(self, user_id: str = "default", top_k: int = 15) -> list[Fact]:
        """获取最重要的记忆事实

        Args:
            user_id: 用户ID
            top_k: 返回数量

        Returns:
            按置信度排序的事实列表
        """
        facts = self.get_facts(user_id)
        return facts[:top_k]

    def clear_memory(self, user_id: str = "default"):
        """清除用户记忆

        Args:
            user_id: 用户ID
        """
        if user_id in self._memories:
            self._memories[user_id] = UserMemory(user_id=user_id)
            self._save()

    def delete_memory(self, user_id: str = "default"):
        """删除用户记忆

        Args:
            user_id: 用户ID
        """
        if user_id in self._memories:
            del self._memories[user_id]
            self._save()

    def list_users(self) -> list[str]:
        """列出所有有记忆的用户ID"""
        return list(self._memories.keys())

    def inject_into_context(self, user_id: str = "default") -> str:
        """生成记忆注入文本

        用于将记忆注入到系统提示中。

        Args:
            user_id: 用户ID

        Returns:
            格式化的记忆文本
        """
        memory = self.get_memory(user_id)
        facts = self.get_recent_facts(user_id)

        lines = ["## 用户记忆"]

        # 上下文
        if memory.work_context:
            lines.append(f"\n**工作上下文**: {memory.work_context}")

        if memory.personal_context:
            lines.append(f"\n**个人上下文**: {memory.personal_context}")

        if memory.top_of_mind:
            lines.append(f"\n**当前关注**: {memory.top_of_mind}")

        # 重要事实
        if facts:
            lines.append("\n**重要事实**:")
            for fact in facts[:10]:
                category_emoji = {
                    "preference": "💡",
                    "knowledge": "📚",
                    "context": "📝",
                    "behavior": "🔄",
                    "goal": "🎯",
                }.get(fact.category, "📌")
                lines.append(f"- {category_emoji} {fact.content}")

        return "\n".join(lines)
