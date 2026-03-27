"""跟踪调用API"""

from fastapi import APIRouter

from echo.research.trace_calls import get_trace_calls


router = APIRouter(prefix="/api/trace", tags=["trace"])


@router.post("/add")
async def add(name: str):
    get_trace_calls().trace(name)
    return {"success": True}
