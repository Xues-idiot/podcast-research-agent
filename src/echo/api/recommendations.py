"""推荐API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.recommendations import get_recommender


router = APIRouter(prefix="/api/recommendations", tags=["recommendations"])


class LearnRequest(BaseModel):
    """学习请求"""
    source: str = ""
    title: str = ""
    platform: str = ""
    tags: list = []


@router.post("/learn")
async def learn_from_research(request: LearnRequest):
    """从研究数据学习偏好

    Args:
        request: 研究数据

    Returns:
        学习结果
    """
    recommender = get_recommender()
    recommender.learn_from_research(request.dict())
    return {"status": "learned"}


@router.get("/")
async def get_recommendations(sources: str, limit: int = 5):
    """获取推荐

    Args:
        sources: 可用的播客源（逗号分隔）
        limit: 返回数量

    Returns:
        推荐列表
    """
    recommender = get_recommender()
    source_list = [s.strip() for s in sources.split(",")]
    recs = recommender.get_recommendations(source_list, limit=limit)

    return {
        "recommendations": [
            {
                "source": r.source,
                "title": r.title,
                "reason": r.reason,
                "score": r.score,
                "platform": r.platform,
            }
            for r in recs
        ],
        "count": len(recs),
    }


@router.get("/similar")
async def get_similar(source: str, all_sources: str, limit: int = 5):
    """获取相似播客

    Args:
        source: 当前播客
        all_sources: 所有播客（逗号分隔）
        limit: 返回数量

    Returns:
        相似播客列表
    """
    recommender = get_recommender()
    source_list = [s.strip() for s in all_sources.split(",")]
    recs = recommender.get_similar_podcasts(source, source_list, limit=limit)

    return {
        "similar": [
            {
                "source": r.source,
                "title": r.title,
                "reason": r.reason,
                "score": r.score,
            }
            for r in recs
        ],
        "count": len(recs),
    }
