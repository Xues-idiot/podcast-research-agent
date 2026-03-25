"""对话历史管理"""

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional

from echo.conversation.types import ChatMessage


class ConversationHistory:
    """对话历史管理器

    支持：
    - 内存存储
    - 持久化到文件系统
    - 对话历史导出
    """

    def __init__(
        self,
        conversation_id: str,
        storage_dir: Optional[str] = None,
        max_messages: int = 50
    ):
        """初始化对话历史管理器

        Args:
            conversation_id: 对话ID
            storage_dir: 存储目录，默认为 ~/.echo/conversations/
            max_messages: 最大保存消息数
        """
        self.conversation_id = conversation_id
        self.max_messages = max_messages
        self.messages: list[ChatMessage] = []

        # 设置存储目录
        if storage_dir:
            self.storage_path = Path(storage_dir) / f"{conversation_id}.json"
        else:
            self.storage_path = Path.home() / ".echo" / "conversations" / f"{conversation_id}.json"

        # 确保目录存在
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

        # 加载历史记录
        self._load()

    def add(self, message: ChatMessage):
        """添加消息"""
        self.messages.append(message)

        # 保持消息数量限制
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

        # 持久化
        self._save()

    def get_recent(self, n: int = 10) -> list[ChatMessage]:
        """获取最近的n条消息"""
        return self.messages[-n:] if self.messages else []

    def get_all(self) -> list[ChatMessage]:
        """获取所有消息"""
        return self.messages.copy()

    def clear(self):
        """清除历史"""
        self.messages.clear()
        self._save()

    def _save(self):
        """保存到文件"""
        data = {
            "conversation_id": self.conversation_id,
            "messages": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "timestamp": msg.timestamp.isoformat(),
                    "references": msg.references
                }
                for msg in self.messages
            ]
        }

        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _load(self):
        """从文件加载"""
        if self.storage_path.exists():
            try:
                with open(self.storage_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                self.messages = [
                    ChatMessage(
                        role=m["role"],
                        content=m["content"],
                        timestamp=datetime.fromisoformat(m["timestamp"]),
                        references=m.get("references", [])
                    )
                    for m in data.get("messages", [])
                ]
            except (json.JSONDecodeError, KeyError):
                # 如果加载失败，初始化空历史
                self.messages = []

    def export_markdown(self) -> str:
        """导出为Markdown格式"""
        lines = [f"# 对话 {self.conversation_id}\n"]

        for msg in self.messages:
            role_emoji = "👤" if msg.role == "user" else "🤖"
            lines.append(f"## {role_emoji} {msg.role}\n")
            lines.append(f"{msg.content}\n")
            lines.append(f"*时间: {msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}*\n")

            if msg.references:
                lines.append("**引用:**")
                for ref in msg.references:
                    lines.append(f"- {ref}")

            lines.append("---\n")

        return "\n".join(lines)
