"""连接API"""

from fastapi import APIRouter

from echo.research.join_tool import get_join_tool


router = APIRouter(prefix="/api/join", tags=["join"])


@router.post("/join")
async def join(items: list, delimiter: str):
    return {"result": get_join_tool().join(items, delimiter)}