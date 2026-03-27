"""三元组工具API"""

from fastapi import APIRouter

from echo.research.triple import get_triple


router = APIRouter(prefix="/api/triple", tags=["triple"])


@router.post("/make")
async def make_triple(first: str, second: str, third: str):
    return {"result": get_triple().make_triple(first, second, third)}


@router.get("/first")
async def get_first(triple: list):
    return {"result": get_triple().get_first(triple)}


@router.get("/second")
async def get_second(triple: list):
    return {"result": get_triple().get_second(triple)}


@router.get("/third")
async def get_third(triple: list):
    return {"result": get_triple().get_third(triple)}