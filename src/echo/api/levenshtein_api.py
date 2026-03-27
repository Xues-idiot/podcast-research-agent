"""编辑距离API"""

from fastapi import APIRouter

from echo.research.levenshtein import get_levenshtein


router = APIRouter(prefix="/api/levenshtein", tags=["levenshtein"])


@router.post("/distance")
async def distance(s1: str, s2: str):
    """编辑距离"""
    tool = get_levenshtein()
    return {"distance": tool.distance(s1, s2)}
