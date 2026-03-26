"""趋势分析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.trends import get_trend_analyzer


router = APIRouter(prefix="/api/trends", tags=["trends"])


class RecordResearchRequest(BaseModel):
    """记录研究请求"""
    id: str
    title: str = ""
    platform: str = ""
    source: str = ""
    tags: list = []
    duration: float = 0


@router.post("/record")
async def record_research(request: RecordResearchRequest):
    """记录研究活动

    Args:
        request: 研究数据

    Returns:
        记录结果
    """
    analyzer = get_trend_analyzer()
    analyzer.record_research(request.dict())
    return {"status": "recorded"}


@router.get("/analyze")
async def analyze_trends(days: int = 30, group_by: str = "day"):
    """分析趋势

    Args:
        days: 分析天数
        group_by: 分组方式

    Returns:
        趋势报告
    """
    analyzer = get_trend_analyzer()
    report = analyzer.analyze(days=days, group_by=group_by)

    return {
        "period": report.period,
        "total_researches": report.total_researches,
        "platform_breakdown": report.platform_breakdown,
        "topic_trends": report.topic_trends,
        "activity_timeline": report.activity_timeline,
        "insights": report.insights,
    }


@router.get("/network")
async def get_topic_network(days: int = 30):
    """获取话题网络

    Args:
        days: 分析天数

    Returns:
        话题网络数据
    """
    analyzer = get_trend_analyzer()
    return analyzer.get_topic_network(days=days)
