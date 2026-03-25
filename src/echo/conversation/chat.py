"""对话处理器 - 处理基于播客内容的问答"""

import asyncio
import uuid
from typing import Any, AsyncIterator, Optional

from openai import AsyncOpenAI

from echo.conversation.history import ConversationHistory
from echo.conversation.prompts import SYSTEM_PROMPT, generate_user_prompt
from echo.conversation.types import ChatMessage, ChatResponse
from echo.config import config


class ConversationHandler:
    """对话处理器

    基于播客研究结果的对话式问答，支持：
    - 多轮对话记忆
    - 引用溯源 (基于知识检索)
    - 流式输出
    """

    def __init__(
        self,
        research_result: dict,
        entries: Optional[list] = None,
        use_retriever: bool = True,
    ):
        """初始化对话处理器

        Args:
            research_result: 研究结果，包含 transcript, summary, keypoints, mindmap 等
            entries: 可选的 Entry 列表，用于向量检索
            use_retriever: 是否使用知识检索器 (默认True)
        """
        self.research_result = research_result
        self.conversation_id = str(uuid.uuid4())[:8]
        self.history = ConversationHistory(self.conversation_id)
        self._context = self._build_context()

        # 初始化LLM客户端
        self._client = AsyncOpenAI(
            api_key=config.minimax.api_key,
            base_url=config.minimax.base_url,
        )
        self._model = config.minimax.model

        # 初始化知识检索器
        self._retriever = None
        if use_retriever and entries:
            from echo.knowledge import KnowledgeRetriever
            self._retriever = KnowledgeRetriever(entries)

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
        retrieved_context = self._retrieve_context(query)

        # 构建提示词
        conversation_history = self.history.get_recent(5)
        user_prompt = generate_user_prompt(
            query=query,
            context=retrieved_context.context_text,
            conversation_history=conversation_history
        )

        # 提取引用信息
        citations = self._format_citations(retrieved_context)

        # 保存用户消息
        self.history.add(ChatMessage(role="user", content=query))

        # 生成回答
        if stream:
            full_answer = ""
            async for chunk in self._stream_generate(user_prompt, citations):
                full_answer += chunk.answer
                yield chunk
            # 保存助手消息
            self.history.add(ChatMessage(role="assistant", content=full_answer))
        else:
            answer = await self._generate(user_prompt)
            self.history.add(ChatMessage(role="assistant", content=answer))
            yield ChatResponse(
                answer=answer,
                references=citations,
                conversation_id=self.conversation_id,
                sources=self._build_sources(retrieved_context),
            )

    async def _stream_generate(
        self,
        prompt: str,
        citations: list[dict],
    ) -> AsyncIterator[ChatResponse]:
        """流式生成回答"""
        # TODO: 集成 MiniMax API 进行流式生成
        # 模拟流式输出
        full_answer = await self._generate(prompt)

        for i in range(0, len(full_answer), 10):
            await asyncio.sleep(0.05)  # 模拟延迟
            yield ChatResponse(
                answer=full_answer[i:i+10],
                conversation_id=self.conversation_id,
                references=citations if i + 10 >= len(full_answer) else [],
            )

    async def _generate(self, prompt: str) -> str:
        """生成回答"""
        try:
            response = await self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM生成失败: {e}")
            return f"抱歉，生成回答时遇到了问题。请稍后重试。"

    def _retrieve_context(self, query: str):
        """检索相关上下文（使用知识检索器）"""
        if self._retriever:
            return self._retriever.retrieve_with_expansion(query, top_k=5, expand_window=1)
        else:
            # 回退到简单实现
            from echo.knowledge import RetrievedContext
            return RetrievedContext(
                query=query,
                context_text=self._context,
                citations=[],
                total_score=0.0,
            )

    def _format_citations(self, retrieved_context) -> list[dict]:
        """格式化引用信息"""
        if not retrieved_context.citations:
            return []

        citations = []
        for i, c in enumerate(retrieved_context.citations, 1):
            citations.append({
                "id": i,
                "entry_id": c.entry_id,
                "start_time": c.start_time,
                "end_time": c.end_time,
                "score": c.score,
                "content": c.content,
            })
        return citations

    def _build_sources(self, retrieved_context) -> list[dict]:
        """构建来源列表"""
        if not retrieved_context.citations:
            return []

        sources = []
        for c in retrieved_context.citations:
            start_min = int(c.start_time // 60)
            start_sec = int(c.start_time % 60)
            sources.append({
                "id": c.entry_id,
                "time": f"{start_min:02d}:{start_sec:02d}",
                "text": c.content[:100] + "..." if len(c.content) > 100 else c.content,
                "relevance": f"{c.score:.0%}",
            })
        return sources

    def get_conversation_id(self) -> str:
        """获取对话ID"""
        return self.conversation_id

    def clear_history(self):
        """清除对话历史"""
        self.history.clear()
