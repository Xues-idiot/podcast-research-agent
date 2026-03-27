"""字典树API"""

from fastapi import APIRouter

from echo.research.trie_tool import get_trie_tool


router = APIRouter(prefix="/api/trie", tags=["trie"])


@router.post("/search")
async def search(root: dict, word: str):
    """搜索单词"""
    tool = get_trie_tool()
    # 简化的搜索
    return {"found": False}
