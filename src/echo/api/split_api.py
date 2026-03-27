"""分割API"""

from fastapi import APIRouter

from echo.research.split_tool import get_split_tool


router = APIRouter(prefix="/api/split", tags=["split"])


@router.post("/split")
async def split(text: str, delimiter: str = None):
    return {"result": get_split_tool().split(text, delimiter)}