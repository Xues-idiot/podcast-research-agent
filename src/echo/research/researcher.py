"""研究代理 - Web研究增强

结合播客内容和Web搜索的研究能力。
使用 Tavily API 进行网络搜索。
"""

import asyncio
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class WebSource:
    """Web来源"""
    url: str
    title: str
    content: str = ""
    published_date: str = ""
    score: float = 0.0


@dataclass
class ResearchResult:
    """研究结果"""
    query: str
    answer: str = ""
    sources: list[WebSource] = field(default_factory=list)
    podcast_insights: list[str] = field(default_factory=list)
    combined_analysis: str = ""
    timestamp: str = ""


class ResearchAgent:
    """研究代理

    结合播客内容和Web搜索，提供增强的研究能力。
    """

    def __init__(self, tavily_api_key: Optional[str] = None):
        """初始化研究代理

        Args:
            tavily_api_key: Tavily API 密钥
        """
        self._tavily_api_key = tavily_api_key

    async def research(
        self,
        query: str,
        podcast_content: Optional[str] = None,
        num_results: int = 5
    ) -> ResearchResult:
        """执行研究

        Args:
            query: 研究查询
            podcast_content: 可选的播客内容（用于结合分析）
            num_results: 返回的结果数量

        Returns:
            ResearchResult: 研究结果
        """
        result = ResearchResult(
            query=query,
            timestamp=datetime.now().isoformat()
        )

        # 执行Web搜索
        sources = await self._search_web(query, num_results)

        # 如果有播客内容，进行结合分析
        if podcast_content:
            result.podcast_insights = await self._analyze_with_podcast(
                query, podcast_content, sources
            )

        # 生成综合答案
        result.combined_analysis = self._generate_analysis(query, sources, result.podcast_insights)
        result.sources = sources

        return result

    async def _search_web(self, query: str, num_results: int = 5) -> list[WebSource]:
        """搜索Web

        Args:
            query: 搜索查询
            num_results: 结果数量

        Returns:
            WebSource 列表
        """
        if not self._tavily_api_key:
            # 如果没有 API Key，返回模拟结果
            return [
                WebSource(
                    url=f"https://example.com/{i}",
                    title=f"结果 {i}",
                    content=" Tavily API 密钥未配置",
                    score=0.5
                )
                for i in range(num_results)
            ]

        try:
            import httpx

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "https://api.tavily.com/search",
                    json={
                        "api_key": self._tavily_api_key,
                        "query": query,
                        "num_results": num_results,
                        "include_answer": True,
                        "include_raw_content": False,
                    },
                    timeout=30.0
                )

                if response.status_code == 200:
                    data = response.json()
                    sources = []

                    for item in data.get("results", []):
                        sources.append(WebSource(
                            url=item.get("url", ""),
                            title=item.get("title", ""),
                            content=item.get("content", "")[:500],
                            published_date=item.get("published_date", ""),
                            score=item.get("score", 0.0)
                        ))

                    return sources

        except Exception as e:
            print(f"Tavily search error: {e}")

        return []

    async def _analyze_with_podcast(
        self,
        query: str,
        podcast_content: str,
        sources: list[WebSource]
    ) -> list[str]:
        """结合播客内容分析

        Args:
            query: 研究查询
            podcast_content: 播客内容
            sources: Web搜索结果

        Returns:
            结合分析得出的见解列表
        """
        # TODO: 使用 LLM 进行结合分析
        # 目前简单返回播客内容的片段
        insights = []

        if len(podcast_content) > 1000:
            # 提取与查询相关的内容片段
            query_lower = query.lower()
            content_lower = podcast_content.lower()

            if query_lower in content_lower:
                # 找到相关段落
                idx = content_lower.find(query_lower)
                start = max(0, idx - 100)
                end = min(len(podcast_content), idx + 200)
                insights.append(f"播客中提到: ...{podcast_content[start:end]}...")

        return insights

    def _generate_analysis(
        self,
        query: str,
        sources: list[WebSource],
        podcast_insights: list[str]
    ) -> str:
        """生成综合分析

        Args:
            query: 研究查询
            sources: Web来源
            podcast_insights: 播客见解

        Returns:
            综合分析文本
        """
        lines = [f"## 关于「{query}」的研究\n"]

        if sources:
            lines.append("### Web 来源\n")
            for i, source in enumerate(sources, 1):
                lines.append(f"{i}. [{source.title}]({source.url})")
                if source.content:
                    lines.append(f"   - {source.content[:200]}...")
                lines.append("")

        if podcast_insights:
            lines.append("### 播客见解\n")
            for insight in podcast_insights:
                lines.append(f"- {insight}")
            lines.append("")

        if not sources and not podcast_insights:
            lines.append("\n暂无相关研究结果。")

        return "\n".join(lines)


class DeepResearcher:
    """深度研究代理

    进行多角度、深入的研究。
    """

    def __init__(self, research_agent: Optional[ResearchAgent] = None):
        """初始化深度研究代理

        Args:
            research_agent: 基础研究代理
        """
        self._research_agent = research_agent or ResearchAgent()

    async def deep_research(
        self,
        topic: str,
        podcast_content: Optional[str] = None,
        angles: Optional[list[str]] = None
    ) -> dict:
        """深度研究

        Args:
            topic: 研究主题
            podcast_content: 播客内容
            angles: 研究角度列表

        Returns:
            多角度研究结果字典
        """
        if angles is None:
            angles = [
                f"{topic} 的定义和背景",
                f"{topic} 的最新发展",
                f"{topic} 的实际应用",
                f"{topic} 的未来趋势",
            ]

        tasks = []
        for angle in angles:
            task = self._research_agent.research(angle, podcast_content)
            tasks.append(task)

        # 并行执行所有研究任务
        results = await asyncio.gather(*tasks)

        return {
            "topic": topic,
            "angles": {
                angle: result
                for angle, result in zip(angles, results)
            },
            "timestamp": datetime.now().isoformat()
        }
