"""质量评分API"""

from fastapi import APIRouter

from echo.research.quality import get_quality_grader


router = APIRouter(prefix="/api/quality", tags=["quality"])


@router.post("/grade")
async def grade_research(research_result: dict):
    """评估研究结果质量

    Args:
        research_result: 研究结果

    Returns:
        质量评分
    """
    grader = get_quality_grader()
    score = grader.grade(research_result)

    return {
        "research_id": score.research_id,
        "overall_score": score.overall_score,
        "tier": grader.get_quality_tier(score.overall_score),
        "completeness": score.completeness,
        "accuracy": score.accuracy,
        "depth": score.depth,
        "citations": score.citations,
        "graded_at": score.graded_at,
    }


@router.get("/tier/{score}")
async def get_tier(score: float):
    """获取分数对应的质量等级

    Args:
        score: 分数

    Returns:
        等级描述
    """
    grader = get_quality_grader()
    return {
        "score": score,
        "tier": grader.get_quality_tier(score),
    }
