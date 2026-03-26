"""搜索增强系统 - 全文搜索和高级筛选"""

import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional


@dataclass
class SearchIndex:
    """搜索索引项"""
    research_id: str = ""
    title: str = ""
    source: str = ""
    platform: str = ""
    summary: str = ""
    keypoints: list = field(default_factory=list)
    full_text: str = ""  # 合并的所有文本
    tags: list = field(default_factory=list)
    created_at: str = ""

    def to_dict(self) -> dict:
        return {
            "research_id": self.research_id,
            "title": self.title,
            "source": self.source,
            "platform": self.platform,
            "summary": self.summary,
            "keypoints": self.keypoints,
            "full_text": self.full_text,
            "tags": self.tags,
            "created_at": self.created_at,
        }


@dataclass
class SearchResult:
    """搜索结果"""
    research_id: str
    title: str
    source: str
    platform: str
    snippet: str  # 匹配片段
    score: float  # 相关性分数
    highlights: list = field(default_factory=list)  # 高亮词


class SearchEngine:
    """搜索引擎"""

    def __init__(self, storage_path: Optional[str] = None):
        """初始化搜索引擎"""
        if storage_path:
            self.storage_path = Path(storage_path)
        else:
            self.storage_path = Path.home() / ".echo" / "search"

        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._index_file = self.storage_path / "index.json"
        self._index: dict[str, SearchIndex] = {}
        self._load()

    def _load(self):
        """加载索引"""
        if self._index_file.exists():
            try:
                with open(self._index_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for rid, item_data in data.items():
                        self._index[rid] = SearchIndex(**item_data)
            except (json.JSONDecodeError, KeyError):
                self._index = {}

    def _save(self):
        """保存索引"""
        data = {rid: item.to_dict() for rid, item in self._index.items()}
        temp_file = self._index_file.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        temp_file.replace(self._index_file)

    def index(
        self,
        research_id: str,
        title: str = "",
        source: str = "",
        platform: str = "",
        summary: str = "",
        keypoints: list = None,
        tags: list = None,
    ):
        """索引研究结果

        Args:
            research_id: 研究ID
            title: 标题
            source: 来源
            platform: 平台
            summary: 摘要
            keypoints: 要点列表
            tags: 标签列表
        """
        keypoints = keypoints or []
        tags = tags or []

        # 合并所有文本用于搜索
        full_text_parts = [title, source, summary]
        full_text_parts.extend(keypoints)
        full_text_parts.extend(tags)
        full_text = " ".join(full_text_parts)

        index_item = SearchIndex(
            research_id=research_id,
            title=title,
            source=source,
            platform=platform,
            summary=summary,
            keypoints=keypoints,
            full_text=full_text.lower(),  # 小写索引
            tags=tags,
            created_at=datetime.now().isoformat(),
        )
        self._index[research_id] = index_item
        self._save()

    def remove(self, research_id: str):
        """移除索引"""
        if research_id in self._index:
            del self._index[research_id]
            self._save()

    def search(
        self,
        query: str,
        platform: Optional[str] = None,
        tag: Optional[str] = None,
        date_from: Optional[str] = None,
        date_to: Optional[str] = None,
        limit: int = 20,
    ) -> list[SearchResult]:
        """搜索

        Args:
            query: 搜索词
            platform: 平台筛选
            tag: 标签筛选
            date_from: 开始日期
            date_to: 结束日期
            limit: 结果数量限制

        Returns:
            搜索结果列表
        """
        query_lower = query.lower()
        query_terms = query_lower.split()

        results = []

        for rid, item in self._index.items():
            # 平台筛选
            if platform and item.platform != platform:
                continue

            # 标签筛选
            if tag and tag not in item.tags:
                continue

            # 日期筛选
            if date_from and item.created_at < date_from:
                continue
            if date_to and item.created_at > date_to:
                continue

            # 计算相关性分数
            score = 0.0
            highlights = []

            # 标题匹配（最高权重）
            if query_lower in item.title.lower():
                score += 10.0
                highlights.append("title")

            # 全文匹配
            full_text = item.full_text
            for term in query_terms:
                if term in full_text:
                    score += full_text.count(term) * 0.5
                    if "content" not in highlights:
                        highlights.append("content")

            # 标签匹配
            for term in query_terms:
                if term in " ".join(item.tags).lower():
                    score += 3.0
                    if "tag" not in highlights:
                        highlights.append("tag")

            # 平台匹配
            if platform and item.platform == platform:
                score += 2.0

            if score > 0:
                # 提取匹配片段
                snippet = self._extract_snippet(item.full_text, query_terms)

                results.append(SearchResult(
                    research_id=rid,
                    title=item.title,
                    source=item.source,
                    platform=item.platform,
                    snippet=snippet,
                    score=score,
                    highlights=highlights,
                ))

        # 按分数排序
        results.sort(key=lambda x: x.score, reverse=True)
        return results[:limit]

    def _extract_snippet(self, text: str, terms: list, context_len: int = 100) -> str:
        """提取匹配片段"""
        text_lower = text.lower()

        # 找到第一个匹配词的位置
        first_match_pos = -1
        for term in terms:
            pos = text_lower.find(term)
            if pos != -1 and (first_match_pos == -1 or pos < first_match_pos):
                first_match_pos = pos

        if first_match_pos == -1:
            return text[:100] + "..." if len(text) > 100 else text

        # 提取上下文
        start = max(0, first_match_pos - context_len)
        end = min(len(text), first_match_pos + context_len)

        snippet = text[start:end]
        if start > 0:
            snippet = "..." + snippet
        if end < len(text):
            snippet = snippet + "..."

        return snippet

    def suggest(self, prefix: str, limit: int = 5) -> list[str]:
        """搜索建议（自动补全）

        Args:
            prefix: 前缀
            limit: 数量限制

        Returns:
            建议列表
        """
        prefix_lower = prefix.lower()
        suggestions = set()

        for item in self._index.values():
            # 标题建议
            if item.title.lower().startswith(prefix_lower):
                suggestions.add(item.title)
            elif prefix_lower in item.title.lower():
                suggestions.add(item.title)

            # 标签建议
            for tag in item.tags:
                if tag.lower().startswith(prefix_lower):
                    suggestions.add(tag)

        return sorted(suggestions)[:limit]

    def get_recent(self, limit: int = 10) -> list[SearchIndex]:
        """获取最近的索引项"""
        items = sorted(
            self._index.values(),
            key=lambda x: x.created_at,
            reverse=True
        )
        return items[:limit]

    def get_platforms(self) -> list[str]:
        """获取所有平台"""
        platforms = set(item.platform for item in self._index.values() if item.platform)
        return sorted(platforms)

    def get_tags(self) -> list[str]:
        """获取所有标签"""
        tags = set()
        for item in self._index.values():
            tags.update(item.tags)
        return sorted(tags)

    def get_stats(self) -> dict:
        """获取索引统计"""
        return {
            "total_indexed": len(self._index),
            "platforms": len(self.get_platforms()),
            "tags": len(self.get_tags()),
        }

    def rebuild_index(self, researches: list[dict]):
        """重建索引

        Args:
            researches: 研究结果列表
        """
        self._index = {}
        for research in researches:
            self.index(
                research_id=research.get("id", ""),
                title=research.get("title", ""),
                source=research.get("source", ""),
                platform=research.get("platform", ""),
                summary=research.get("summary", {}).get("content", ""),
                keypoints=[kp.get("content", "") for kp in research.get("keypoints", [])],
                tags=research.get("tags", []),
            )


# 全局实例
_search_engine: Optional[SearchEngine] = None


def get_search_engine() -> SearchEngine:
    """获取全局搜索引擎"""
    global _search_engine
    if _search_engine is None:
        _search_engine = SearchEngine()
    return _search_engine
