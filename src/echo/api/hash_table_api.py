"""哈希表API"""

from fastapi import APIRouter

from echo.research.hash_table import get_hash_table


router = APIRouter(prefix="/api/hash-table", tags=["hash-table"])


@router.post("/create")
async def create(size: int = 100):
    """创建哈希表"""
    tool = get_hash_table()
    return {"table": tool.create(size)}


@router.post("/put")
async def put(table: list, key: str, value: str):
    """插入"""
    tool = get_hash_table()
    tool.put(table, key, value)
    return {"success": True}
