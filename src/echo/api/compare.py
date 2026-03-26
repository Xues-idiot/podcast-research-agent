"""研究结果对比API"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.comparator import get_comparator


router = APIRouter(prefix="/api/compare", tags=["compare"])


class CompareRequest(BaseModel):
    """对比请求"""
    result_a: dict  # 第一个播客的研究结果
    result_b: dict  # 第二个播客的研究结果


class CompareByIdRequest(BaseModel):
    """通过ID对比请求"""
    podcast_id_a: str
    podcast_id_b: str


@router.post("/")
async def compare_results(request: CompareRequest):
    """对比两个研究结果

    Args:
        request: 包含两个研究结果的请求

    Returns:
        对比结果
    """
    comparator = get_comparator()
    result = comparator.compare(request.result_a, request.result_b)

    return {
        "topic_overlap": result.topic_overlap,
        "keypoint_similarity": result.keypoint_similarity,
        "content_length_ratio": result.content_length_ratio,
        "shared_concepts": result.shared_concepts,
        "unique_insights_a": result.unique_insights_a,
        "unique_insights_b": result.unique_insights_b,
        "summary": result.summary,
    }
