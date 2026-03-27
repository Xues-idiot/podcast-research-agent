"""组合函数API"""

from fastapi import APIRouter

from echo.research.compose_func import get_compose_func


router = APIRouter(prefix="/api/compose", tags=["compose"])


@router.post("/compose")
async def compose():
    return {"result": None}
