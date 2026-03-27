"""流式处理API"""

from fastapi import APIRouter

from echo.research.stream_tool import get_stream_tool


router = APIRouter(prefix="/api/stream", tags=["stream"])


@router.post("/filter")
async def filter_stream(items: list, pred: str):
    """流式过滤"""
    tool = get_stream_tool()
    pred_func = eval(pred)
    return {"items": list(tool.filter_stream(items, pred_func))}
