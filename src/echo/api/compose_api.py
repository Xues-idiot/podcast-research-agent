"""组合API"""

from fastapi import APIRouter

from echo.research.compose_tool import get_compose_tool


router = APIRouter(prefix="/api/compose", tags=["compose"])


@router.post("/compose")
async def compose(*funcs):
    return {"result": get_compose_tool().compose(*funcs)}