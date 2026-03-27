"""集合操作API"""

from fastapi import APIRouter

from echo.research.set_ops import get_set_ops


router = APIRouter(prefix="/api/set-ops", tags=["set-ops"])


@router.post("/union")
async def union(set1: list, set2: list):
    return {"result": get_set_ops().union(set1, set2)}


@router.post("/intersection")
async def intersection(set1: list, set2: list):
    return {"result": get_set_ops().intersection(set1, set2)}


@router.post("/difference")
async def difference(set1: list, set2: list):
    return {"result": get_set_ops().difference(set1, set2)}