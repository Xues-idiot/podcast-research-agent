"""单次调用API"""

from fastapi import APIRouter

from echo.research.once_call import get_once_call_tool


router = APIRouter(prefix="/api/once-call", tags=["once-call"])


@router.post("/once")
async def once():
    tool = get_once_call_tool()
    return {"message": "Once call configured"}