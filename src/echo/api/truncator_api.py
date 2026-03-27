"""截断API"""

from fastapi import APIRouter

from echo.research.truncator_tool import get_truncator_tool


router = APIRouter(prefix="/api/truncator", tags=["truncator"])


@router.post("/truncate")
async def truncate(text: str, length: int, suffix: str = "..."):
    return {"result": get_truncator_tool().truncate(text, length, suffix)}