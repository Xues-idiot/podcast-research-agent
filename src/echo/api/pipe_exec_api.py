"""管道执行API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.pipe_exec import get_pipe_exec_tool


router = APIRouter(prefix="/api/pipe-exec", tags=["pipe-exec"])


class PipeRequest(BaseModel):
    value: Any
    funcs: List[str]


@router.post("/pipe")
async def pipe(request: PipeRequest):
    tool = get_pipe_exec_tool()
    return {"message": "Pipe configured", "func_count": len(request.funcs)}