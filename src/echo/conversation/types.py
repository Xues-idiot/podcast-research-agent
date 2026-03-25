"""对话类型定义"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class ChatMessage:
    """对话消息"""
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    references: list = field(default_factory=list)


@dataclass
class ChatResponse:
    """聊天响应"""
    answer: str
    conversation_id: str
    sources: list = field(default_factory=list)
    message_id: Optional[str] = None