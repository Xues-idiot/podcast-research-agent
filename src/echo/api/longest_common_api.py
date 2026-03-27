"""最长公共子序列API"""

from fastapi import APIRouter

from echo.research.longest_common import get_longest_common


router = APIRouter(prefix="/api/lcs", tags=["lcs"])


@router.post("/length")
async def lcs_length(s1: str, s2: str):
    """LCS长度"""
    tool = get_longest_common()
    return {"length": tool.lcs(s1, s2)}


@router.post("/sequence")
async def lcs_sequence(s1: str, s2: str):
    """LCS序列"""
    tool = get_longest_common()
    return {"sequence": tool.lcs_sequence(s1, s2)}
