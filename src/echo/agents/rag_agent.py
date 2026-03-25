"""Agent+RAG融合代理

结合Agent能力和RAG检索，增强研究能力。
参考 RAGFlow 的 Agent+RAG 融合架构。
"""

from dataclasses import dataclass, field
from typing import Optional, Any
from echo.knowledge import KnowledgeRetriever, HybridRetriever
from echo.conversation import ConversationHandler


@dataclass
class AgentConfig:
    """Agent配置"""
    model_name: str = "MiniMax-M2.7"
    temperature: float = 0.7
    max_tokens: int = 4096
    enable_rag: bool = True
    enable_citation: bool = True
    retrieval_top_k: int = 5


@dataclass
class RAGResponse:
    """RAG增强响应"""
    answer: str
    citations: list = field(default_factory=list)
    sources: list = field(default_factory=list)
    retrieved_context: str = ""
    agent_metadata: dict = field(default_factory=dict)


class RAGAgent:
    """RAG增强Agent

    结合知识库检索和Agent生成能力：
    1. 用户查询 → 知识库检索 → 增强上下文
    2. 增强上下文 → Agent生成 → 带引用的回答
    """

    def __init__(
        self,
        config: Optional[AgentConfig] = None,
        knowledge_retriever: Optional[KnowledgeRetriever] = None,
        conversation_handler: Optional[ConversationHandler] = None,
    ):
        """初始化RAG Agent

        Args:
            config: Agent配置
            knowledge_retriever: 知识检索器
            conversation_handler: 对话处理器
        """
        self.config = config or AgentConfig()
        self._retriever = knowledge_retriever
        self._conversation = conversation_handler

    def set_retriever(self, retriever: KnowledgeRetriever):
        """设置知识检索器

        Args:
            retriever: 知识检索器实例
        """
        self._retriever = retriever

    def set_conversation(self, handler: ConversationHandler):
        """设置对话处理器

        Args:
            handler: 对话处理器实例
        """
        self._conversation = handler

    async def query(
        self,
        query: str,
        podcast_id: Optional[str] = None,
        stream: bool = False,
    ) -> RAGResponse:
        """查询

        Args:
            query: 用户查询
            podcast_id: 可选的播客ID（用于限定检索范围）
            stream: 是否流式返回

        Returns:
            RAGResponse: RAG增强的响应
        """
        citations = []
        retrieved_context = ""

        # 1. 知识库检索
        if self._retriever and self.config.enable_rag:
            try:
                context = await self._retriever.retrieve(
                    query=query,
                    top_k=self.config.retrieval_top_k,
                    include_metadata=True,
                )
                retrieved_context = context.context_text
                citations = [
                    {
                        "entry_id": c.entry_id,
                        "content": c.content,
                        "start_time": c.start_time,
                        "end_time": c.end_time,
                        "score": c.score,
                    }
                    for c in context.citations
                ]
            except Exception as e:
                print(f"Retrieval error: {e}")

        # 2. 对话生成
        answer = ""
        if self._conversation:
            try:
                async for event in self._conversation.chat(
                    query=query,
                    entries=[],  # 可以传入相关entries
                    stream=stream,
                    use_retriever=False,  # 已经在retriever中处理了
                ):
                    if not stream:
                        if hasattr(event, 'answer'):
                            answer = event.answer
                        elif isinstance(event, dict):
                            answer = event.get("answer", "")
                    else:
                        # 流式处理
                        if hasattr(event, 'delta'):
                            answer += event.delta
                        elif isinstance(event, dict):
                            answer += event.get("delta", "")
            except Exception as e:
                print(f"Conversation error: {e}")
                answer = f"处理查询时发生错误: {str(e)}"
        else:
            # 没有对话处理器时的简单回复
            answer = self._generate_simple_answer(query, retrieved_context)

        # 3. 构建响应
        return RAGResponse(
            answer=answer,
            citations=citations,
            sources=[c["entry_id"] for c in citations],
            retrieved_context=retrieved_context,
            agent_metadata={
                "model": self.config.model_name,
                "rag_enabled": self.config.enable_rag,
                "retrieval_count": len(citations),
            },
        )

    def _generate_simple_answer(self, query: str, context: str) -> str:
        """生成简单回答

        当没有对话处理器时使用。

        Args:
            query: 用户查询
            context: 检索到的上下文

        Returns:
            简单回答
        """
        if context:
            return f"根据检索到的内容，关于「{query}」的信息如下：\n\n{context[:500]}...\n\n（注意：这是简化回答，建议配置对话处理器以获得完整功能）"
        return f"关于「{query}」，我没有找到相关的内容。请提供更多信息或尝试其他查询。"

    async def batch_query(
        self,
        queries: list[str],
        podcast_id: Optional[str] = None,
    ) -> list[RAGResponse]:
        """批量查询

        Args:
            queries: 查询列表
            podcast_id: 可选的播客ID

        Returns:
            RAGResponse 列表
        """
        import asyncio

        tasks = [self.query(q, podcast_id) for q in queries]
        return await asyncio.gather(*tasks)


class ResearchRAGAgent(RAGAgent):
    """研究增强RAG Agent

    专门用于播客研究的RAG Agent，
    支持多源检索和深度分析。
    """

    def __init__(self, config: Optional[AgentConfig] = None):
        """初始化研究RAG Agent

        Args:
            config: Agent配置
        """
        super().__init__(config)
        self._research_mode = False

    async def research_query(
        self,
        query: str,
        podcast_content: str,
        podcast_id: Optional[str] = None,
    ) -> RAGResponse:
        """研究查询

        结合播客内容和知识库进行深度研究。

        Args:
            query: 研究查询
            podcast_content: 播客内容
            podcast_id: 播客ID

        Returns:
            RAGResponse: 研究响应
        """
        # 增强上下文：结合播客内容
        enhanced_context = podcast_content

        if self._retriever:
            try:
                context = await self._retriever.retrieve(
                    query=query,
                    top_k=self.config.retrieval_top_k,
                    include_metadata=True,
                )
                if context.context_text:
                    enhanced_context = f"## 播客内容\n{podcast_content[:2000]}\n\n## 相关知识\n{context.context_text}"
            except Exception:
                pass

        # 生成研究回答
        answer = f"## 研究结果：{query}\n\n"

        if enhanced_context:
            answer += f"### 综合分析\n基于播客内容和知识库检索，{self._analyze(query, enhanced_context)}\n"
        else:
            answer += f"关于「{query}」的分析已完成，但没有找到足够的上下文信息。"

        return RAGResponse(
            answer=answer,
            citations=[],
            sources=[],
            retrieved_context=enhanced_context,
            agent_metadata={
                "mode": "research",
                "model": self.config.model_name,
            },
        )

    def _analyze(self, query: str, context: str) -> str:
        """简单分析

        Args:
            query: 查询
            context: 上下文

        Returns:
            分析结果
        """
        # TODO: 使用 LLM 进行深度分析
        return f"针对「{query}」，在给定的上下文中找到了一些相关信息。详细内容请查看上下文。"
