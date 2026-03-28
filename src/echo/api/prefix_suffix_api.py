"""前缀后缀API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.prefix_suffix import get_prefix_suffix_tool


router = APIRouter(prefix="/api/prefix-suffix", tags=["prefix-suffix"])


class PrefixSuffixRequest(BaseModel):
    text: str
    value: str


@router.post("/add-prefix")
async def add_prefix(request: PrefixSuffixRequest):
    tool = get_prefix_suffix_tool()
    return {"result": tool.add_prefix(request.text, request.value)}


@router.post("/add-suffix")
async def add_suffix(request: PrefixSuffixRequest):
    tool = get_prefix_suffix_tool()
    return {"result": tool.add_suffix(request.text, request.value)}


@router.post("/remove-prefix")
async def remove_prefix(request: PrefixSuffixRequest):
    tool = get_prefix_suffix_tool()
    return {"result": tool.remove_prefix(request.text, request.value)}


@router.post("/remove-suffix")
async def remove_suffix(request: PrefixSuffixRequest):
    tool = get_prefix_suffix_tool()
    return {"result": tool.remove_suffix(request.text, request.value)}