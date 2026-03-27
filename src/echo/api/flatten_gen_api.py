"""扁平化生成API"""

from fastapi import APIRouter

from echo.research.flatten_gen import get_flatten_gen


router = APIRouter(prefix="/api/flatten-gen", tags=["flatten-gen"])


@router.post("/flatten")
async def flatten(items: list):
    """深度扁平化"""
    tool = get_flatten_gen()
    return {"result": tool.flatten(items)}
