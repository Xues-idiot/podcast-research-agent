"""研究API - Web研究增强路由"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

from echo.research import ResearchAgent, DeepResearcher


router = APIRouter(prefix="/api/research", tags=["research"])


# 研究代理实例
_research_agent = ResearchAgent()
_deep_researcher = DeepResearcher(_research_agent)


class ResearchRequest(BaseModel):
    """研究请求"""
    query: str
    podcast_content: Optional[str] = None
    num_results: int = 5


class DeepResearchRequest(BaseModel):
    """深度研究请求"""
    topic: str
    podcast_content: Optional[str] = None
    angles: list[str] = []


@router.post("/search")
async def web_search(request: ResearchRequest):
    """执行Web研究

    Args:
        request: 研究请求

    Returns:
        研究结果
    """
    result = await _research_agent.research(
        query=request.query,
        podcast_content=request.podcast_content,
        num_results=request.num_results
    )

    return {
        "query": result.query,
        "answer": result.answer,
        "sources": [
            {
                "url": s.url,
                "title": s.title,
                "content": s.content,
                "published_date": s.published_date,
                "score": s.score,
            }
            for s in result.sources
        ],
        "podcast_insights": result.podcast_insights,
        "combined_analysis": result.combined_analysis,
        "timestamp": result.timestamp,
    }


@router.post("/deep")
async def deep_research(request: DeepResearchRequest):
    """执行深度研究

    Args:
        request: 深度研究请求

    Returns:
        多角度研究结果
    """
    result = await _deep_researcher.deep_research(
        topic=request.topic,
        podcast_content=request.podcast_content,
        angles=request.angles if request.angles else None
    )

    return {
        "topic": result["topic"],
        "angles": {
            angle: {
                "sources": [
                    {
                        "url": s.url,
                        "title": s.title,
                        "content": s.content,
                    }
                    for s in r.sources
                ],
                "podcast_insights": r.podcast_insights,
                "combined_analysis": r.combined_analysis,
            }
            for angle, r in result["angles"].items()
        },
        "timestamp": result["timestamp"],
    }


@router.get("/sources")
async def list_sources():
    """列出可用的研究来源

    Returns:
        来源列表
    """
    return {
        "sources": [
            {"name": "Tavily", "type": "web_search", "enabled": True},
            {"name": "Podcast Content", "type": "internal", "enabled": True},
        ]
    }
