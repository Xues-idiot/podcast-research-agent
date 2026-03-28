"""空白字符处理API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.whitespace import get_whitespace_tool


router = APIRouter(prefix="/api/whitespace", tags=["whitespace"])


class ProcessRequest(BaseModel):
    text: str


@router.post("/remove-extra")
async def remove_extra(request: ProcessRequest):
    tool = get_whitespace_tool()
    return {"result": tool.remove_extra_spaces(request.text)}


@router.post("/normalize")
async def normalize(request: ProcessRequest):
    tool = get_whitespace_tool()
    return {"result": tool.normalize_spaces(request.text)}


@router.post("/remove-all")
async def remove_all(request: ProcessRequest):
    tool = get_whitespace_tool()
    return {"result": tool.remove_all_spaces(request.text)}


@router.post("/split-lines")
async def split_lines(request: ProcessRequest):
    tool = get_whitespace_tool()
    return {"result": tool.split_lines(request.text)}