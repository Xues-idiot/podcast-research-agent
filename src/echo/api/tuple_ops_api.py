"""元组操作API"""

from fastapi import APIRouter

from echo.research.tuple_ops import get_tuple_ops


router = APIRouter(prefix="/api/tuple-ops", tags=["tuple-ops"])


@router.post("/make")
async def make_tuple(*items):
    return {"result": get_tuple_ops().make_tuple(*items)}


@router.get("/first")
async def get_first(tuple_data: list):
    return {"result": get_tuple_ops().get_first(tuple_data)}


@router.get("/last")
async def get_last(tuple_data: list):
    return {"result": get_tuple_ops().get_last(tuple_data)}