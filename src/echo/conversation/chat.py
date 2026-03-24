"""对话处理器 - 处理基于播客内容的问答"""

import asyncio
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, AsyncIterator, Optional

from echo.conversation.history import ConversationHistory
from echo.conversation.prompts import SYSTEM_PROMPT, generate_user_prompt


@dataclass
class ChatMessage:
    """对话消息"""
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    references: list[dict] = field(default_factory=list)


@dataclass
class ChatResponse:
    """聊天响应"""
    answer: str
    references: list[dict] = field(default_factory=list)
    conversation_id: str = ""


class ConversationHandler:
    """对话处理器

    基于播客研究结果的对话式问答，支持：
    - 多轮对话记忆
    - 引用溯源
    - 流式输出
    """

    def __init__(self, research_result: dict):
        """初始化对话处理器

        Args:
            research_result: 研究结果，包含 transcript, summary, keypoints, mindmap 等
        """
        self.research_result = research_result
        self.conversation_id = str(uuid.uuid4())[:8]
        self.history = ConversationHistory(self.conversation_id)
        self._context = self._build_context()

    def _build_context(self) -> str:
        """从研究结果构建上下文"""
        parts = []

        # 添加摘要
        if summary := self.research_result.get("summary"):
            parts.append(f"【内容摘要】\n{summary.get('summary', '')}")

        # 添加关键要点
        if keypoints := self.research_result.get("keypoints"):
            kp_text = "\n".join([f"- {kp['content']}" for kp in keypoints])
            parts.append(f"【关键要点】\n{kp_text}")

        # 添加思维导图
        if mindmap := self.research_result.get("mindmap"):
            parts.append(f"【主题】{mindmap.get('root', '')}")
            for branch in mindmap.get("branches", []):
                children = ", ".join(branch.get("children", []))
                parts.append(f"- {branch['title']}: {children}")

        # 添加转录文本（截取关键部分）
        if transcript := self.research_result.get("transcript"):
            text = transcript.get("text", "")
            # 保留前4000字符作为上下文
            if len(text) > 4000:
                text = text[:4000] + "\n[...截断...]"
            parts.append(f"【转录文本】\n{text}")

        return "\n\n".join(parts)

    async def chat(
        self,
        query: str,
        stream: bool = True
    ) -> AsyncIterator[ChatResponse]:
        """处理用户问题

        Args:
            query: 用户问题
            stream: 是否流式输出

        Yields:
            ChatResponse: 回答片段
        """
        # 检索相关上下文
        relevant_context = self._retrieve_context(query)

        # 构建提示词
        conversation_history = self.history.get_recent(5)
        user_prompt = generate_user_prompt(
            query=query,
            context=relevant_context,
            conversation_history=conversation_history
        )

        # 生成回答
        if stream:
            async for chunk in self._stream_generate(user_prompt):
                yield chunk
        else:
            answer = await self._generate(user_prompt)
            yield ChatResponse(
                answer=answer,
                references=self._extract_references(relevant_context),
                conversation_id=self.conversation_id
            )

        # 保存对话历史
        self.history.add(ChatMessage(role="user", content=query))
        self.history.add(ChatMessage(role="assistant", content=await self._generate(user_prompt)))

    async def _stream_generate(self, prompt: str) -> AsyncIterator[ChatResponse]:
        """流式生成回答"""
        # TODO: 集成 MiniMax API 进行流式生成
        # 模拟流式输出
        full_answer = await self._generate(prompt)

        for i in range(0, len(full_answer), 10):
            await asyncio.sleep(0.05)  # 模拟延迟
            yield ChatResponse(
                answer=full_answer[i:i+10],
                conversation_id=self.conversation_id
            )

    async def _generate(self, prompt: str) -> str:
        """生成回答"""
        # TODO: 调用 MiniMax API
        # 暂时返回模拟回答
        return f"这是基于播客内容的回答。关于您的问题，我需要查阅相关资料后给出准确的答复。"

    def _retrieve_context(self, query: str) -> str:
        """检索相关上下文（简单关键词匹配）"""
        # 简单实现：直接返回全部上下文
        # TODO: 实现向量检索
        return self._context

    def _extract_references(self, context: str) -> list[dict]:
        """提取引用"""
        # 简单实现：返回空引用
        # TODO: 实现精确引用追踪
        return []

    def get_conversation_id(self) -> str:
        """获取对话ID"""
        return self.conversation_id

    def clear_history(self):
        """清除对话历史"""
        self.history.clear()
