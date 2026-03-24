"""知识检索模块 - 支持引用追踪的语义检索

集成 Bi-encoder 实现语义检索，并追踪每个检索结果的信息来源。
"""

from dataclasses import dataclass, field
from typing import Optional
import numpy as np

from echo.knowledge.entry import Entry
from echo.knowledge.bi_encoder import BiEncoder


@dataclass
class Citation:
    """引用信息"""
    entry_id: str
    content: str
    start_time: float
    end_time: float
    score: float
    metadata: dict = field(default_factory=dict)


@dataclass
class RetrievedContext:
    """检索到的上下文"""
    query: str
    context_text: str
    citations: list[Citation]
    total_score: float


class KnowledgeRetriever:
    """知识检索器

    结合向量检索和关键词匹配，实现精准的知识检索，
    并追踪每个结果的信息来源。
    """

    def __init__(
        self,
        entries: list[Entry],
        encoder: Optional[BiEncoder] = None,
        min_score: float = 0.3,
    ):
        """初始化检索器

        Args:
            entries: Entry列表
            encoder: Bi-encoder实例 (None则创建默认实例)
            min_score: 最小相似度阈值
        """
        self.entries = entries
        self.encoder = encoder or BiEncoder()
        self.min_score = min_score
        self._entry_texts: dict[str, str] = {e.id: e.compiled for e in entries}

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        include_metadata: bool = True,
    ) -> RetrievedContext:
        """检索相关上下文

        Args:
            query: 查询文本
            top_k: 返回数量
            include_metadata: 是否包含元数据

        Returns:
            RetrievedContext: 检索结果和引用信息
        """
        if not self.entries:
            return RetrievedContext(
                query=query,
                context_text="",
                citations=[],
                total_score=0.0,
            )

        # 向量检索
        results = self.encoder.search(
            query=query,
            entries=self.entries,
            top_k=top_k,
            min_score=self.min_score,
        )

        if not results:
            return RetrievedContext(
                query=query,
                context_text="",
                citations=[],
                total_score=0.0,
            )

        # 构建引用和上下文
        citations = []
        context_parts = []
        total_score = 0.0

        for entry, score in results:
            citation = Citation(
                entry_id=entry.id,
                content=entry.raw[:200] + "..." if len(entry.raw) > 200 else entry.raw,
                start_time=entry.start_time,
                end_time=entry.end_time,
                score=float(score),
                metadata=entry.metadata if include_metadata else {},
            )
            citations.append(citation)
            total_score += float(score)

            # 时间戳标记
            start_min = int(entry.start_time // 60)
            start_sec = int(entry.start_time % 60)
            time_marker = f"[{start_min:02d}:{start_sec:02d}]"

            context_parts.append(f"{time_marker} {entry.compiled}")

        context_text = "\n\n".join(context_parts)

        return RetrievedContext(
            query=query,
            context_text=context_text,
            citations=citations,
            total_score=total_score / len(citations) if citations else 0.0,
        )

    def retrieve_with_expansion(
        self,
        query: str,
        top_k: int = 5,
        expand_window: int = 1,
    ) -> RetrievedContext:
        """扩展检索 - 包含相邻片段

        Args:
            query: 查询文本
            top_k: 返回数量
            expand_window: 前后扩展的片段数

        Returns:
            RetrievedContext: 扩展后的检索结果
        """
        base_result = self.retrieve(query, top_k * (expand_window * 2 + 1))

        if not base_result.citations:
            return base_result

        # 按时间排序
        sorted_citations = sorted(base_result.citations, key=lambda c: c.start_time)

        # 选择最相关的片段及其邻居
        selected_ids = set()
        for citation in base_result.citations[:top_k]:
            selected_ids.add(citation.entry_id)
            # 添加相邻片段
            for i, entry_citation in enumerate(sorted_citations):
                if entry_citation.entry_id == citation.entry_id:
                    for j in range(max(0, i - expand_window), min(len(sorted_citations), i + expand_window + 1)):
                        selected_ids.add(sorted_citations[j].entry_id)
                    break

        # 构建扩展上下文
        expanded_entries = [e for e in self.entries if e.id in selected_ids]
        expanded_entries.sort(key=lambda e: e.start_time)

        context_parts = []
        for entry in expanded_entries:
            start_min = int(entry.start_time // 60)
            start_sec = int(entry.start_time % 60)
            time_marker = f"[{start_min:02d}:{start_sec:02d}]"
            context_parts.append(f"{time_marker} {entry.compiled}")

        expanded_context = "\n\n".join(context_parts)

        # 重新计算分数
        new_citations = []
        for c in base_result.citations:
            if c.entry_id in selected_ids:
                new_citations.append(c)

        return RetrievedContext(
            query=query,
            context_text=expanded_context,
            citations=new_citations,
            total_score=sum(c.score for c in new_citations) / len(new_citations) if new_citations else 0.0,
        )

    def format_citations_for_display(self, citations: list[Citation]) -> str:
        """格式化引用用于显示

        Args:
            citations: 引用列表

        Returns:
            格式化字符串
        """
        if not citations:
            return "无引用"

        lines = ["**参考来源:**"]
        for i, c in enumerate(citations, 1):
            start_min = int(c.start_time // 60)
            start_sec = int(c.start_time % 60)
            lines.append(
                f"{i}. [{start_min:02d}:{start_sec:02d}] "
                f"{c.content[:100]}... (相关度: {c.score:.2f})"
            )

        return "\n".join(lines)


class HybridRetriever:
    """混合检索器

    结合向量检索和关键词检索，提高检索精度。
    """

    def __init__(
        self,
        entries: list[Entry],
        encoder: Optional[BiEncoder] = None,
        vector_weight: float = 0.7,
        keyword_weight: float = 0.3,
    ):
        """初始化混合检索器

        Args:
            entries: Entry列表
            encoder: Bi-encoder实例
            vector_weight: 向量检索权重
            keyword_weight: 关键词检索权重
        """
        self.entries = entries
        self.encoder = encoder or BiEncoder()
        self.vector_weight = vector_weight
        self.keyword_weight = keyword_weight

    def _keyword_search(self, query: str, top_k: int) -> list[tuple[Entry, float]]:
        """关键词检索 (BM25)"""
        # 简单实现：词重叠计数
        query_words = set(query.lower().split())
        scores = []

        for entry in self.entries:
            entry_words = set(entry.compiled.lower().split())
            overlap = len(query_words & entry_words)
            if overlap > 0:
                score = overlap / len(query_words)
                scores.append((entry, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> RetrievedContext:
        """混合检索

        Args:
            query: 查询文本
            top_k: 返回数量

        Returns:
            RetrievedContext: 检索结果
        """
        # 向量检索
        vector_results = self.encoder.search(
            query=query,
            entries=self.entries,
            top_k=top_k * 2,
            min_score=0.0,
        )

        # 关键词检索
        keyword_results = self._keyword_search(query, top_k * 2)

        # 合并分数
        entry_scores: dict[str, tuple[Entry, float]] = {}

        for entry, score in vector_results:
            entry_scores[entry.id] = (entry, score * self.vector_weight)

        for entry, score in keyword_results:
            if entry.id in entry_scores:
                e, s = entry_scores[entry.id]
                entry_scores[entry.id] = (e, s + score * self.keyword_weight)
            else:
                entry_scores[entry.id] = (entry, score * self.keyword_weight)

        # 排序并取top_k
        sorted_results = sorted(
            entry_scores.values(),
            key=lambda x: x[1],
            reverse=True
        )[:top_k]

        if not sorted_results:
            return RetrievedContext(
                query=query,
                context_text="",
                citations=[],
                total_score=0.0,
            )

        # 构建结果
        citations = []
        context_parts = []
        total_score = 0.0

        for entry, score in sorted_results:
            if score < 0.1:
                continue

            citation = Citation(
                entry_id=entry.id,
                content=entry.raw[:200] + "..." if len(entry.raw) > 200 else entry.raw,
                start_time=entry.start_time,
                end_time=entry.end_time,
                score=score,
                metadata=entry.metadata,
            )
            citations.append(citation)
            total_score += score

            start_min = int(entry.start_time // 60)
            start_sec = int(entry.start_time % 60)
            time_marker = f"[{start_min:02d}:{start_sec:02d}]"
            context_parts.append(f"{time_marker} {entry.compiled}")

        context_text = "\n\n".join(context_parts)

        return RetrievedContext(
            query=query,
            context_text=context_text,
            citations=citations,
            total_score=total_score / len(citations) if citations else 0.0,
        )
