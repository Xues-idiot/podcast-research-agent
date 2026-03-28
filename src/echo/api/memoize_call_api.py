"""记忆化API"""

from fastapi import APIRouter

from echo.research.memoize_call import get_memoize_call_tool


router = APIRouter(prefix="/api/memoize-call", tags=["memoize-call"])


@router.post("/memoize")
async def memoize():
    tool = get_memoize_call_tool()
    return {"message": "Memoize configured"}