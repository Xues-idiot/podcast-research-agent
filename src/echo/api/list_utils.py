"""列表工具API"""

from fastapi import APIRouter

from echo.research.list_utils import get_list_utils


router = APIRouter(prefix="/api/list", tags=["list"])


@router.post("/unique")
async def unique(items: list):
    return {"result": get_list_utils().unique(items)}


@router.post("/chunk")
async def chunk(items: list, chunk_size: int):
    return {"result": get_list_utils().chunk(items, chunk_size)}


@router.post("/flatten")
async def flatten(nested: list[list]):
    return {"result": get_list_utils().flatten(nested)}


@router.post("/intersection")
async def intersection(list1: list, list2: list):
    return {"result": get_list_utils().intersection(list1, list2)}


@router.post("/union")
async def union(list1: list, list2: list):
    return {"result": get_list_utils().union(list1, list2)}


@router.post("/difference")
async def difference(list1: list, list2: list):
    return {"result": get_list_utils().difference(list1, list2)}