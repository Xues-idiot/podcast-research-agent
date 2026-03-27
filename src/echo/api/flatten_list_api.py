"""扁平化API"""

from fastapi import APIRouter

from echo.research.flatten_list import get_flatten_list


router = APIRouter(prefix="/api/flatten", tags=["flatten"])


@router.post("/deep")
async def flatten_deep(items: list):
    """深度扁平化"""
    tool = get_flatten_list()
    return {"items": tool.flatten(items)}


@router.post("/once")
async def flatten_once(items: list):
    """单层扁平化"""
    tool = get_flatten_list()
    return {"items": tool.flatten_once(items)}
