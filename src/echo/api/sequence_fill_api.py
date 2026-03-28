"""序列填充API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

from echo.research.sequence_fill import get_sequence_fill_tool


router = APIRouter(prefix="/api/sequence-fill", tags=["sequence-fill"])


class FillRequest(BaseModel):
    items: List[Any]
    fill_value: Any = None


@router.post("/forward")
async def fill_forward(request: FillRequest):
    tool = get_sequence_fill_tool()
    return {"result": tool.fill_forward(request.items, request.fill_value)}


@router.post("/backward")
async def fill_backward(request: FillRequest):
    tool = get_sequence_fill_tool()
    return {"result": tool.fill_backward(request.items, request.fill_value)}


@router.post("/linear")
async def fill_linear(request: FillRequest):
    tool = get_sequence_fill_tool()
    return {"result": tool.fill_linear(request.items)}