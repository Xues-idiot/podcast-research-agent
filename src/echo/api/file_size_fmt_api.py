"""文件大小格式化API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.file_size_fmt import get_file_size_fmt_tool


router = APIRouter(prefix="/api/file-size-fmt", tags=["file-size-fmt"])


class BytesRequest(BaseModel):
    bytes_val: int
    precision: int = 2


@router.post("/format")
async def format_bytes(request: BytesRequest):
    tool = get_file_size_fmt_tool()
    return {"result": tool.format_bytes(request.bytes_val, request.precision)}


class ParseSizeRequest(BaseModel):
    size_str: str


@router.post("/parse")
async def parse_size(request: ParseSizeRequest):
    tool = get_file_size_fmt_tool()
    return {"result": tool.parse_size(request.size_str)}


@router.post("/to-kb")
async def to_kb(request: BytesRequest):
    tool = get_file_size_fmt_tool()
    return {"result": tool.bytes_to_kb(request.bytes_val)}


@router.post("/to-mb")
async def to_mb(request: BytesRequest):
    tool = get_file_size_fmt_tool()
    return {"result": tool.bytes_to_mb(request.bytes_val)}


@router.post("/to-gb")
async def to_gb(request: BytesRequest):
    tool = get_file_size_fmt_tool()
    return {"result": tool.bytes_to_gb(request.bytes_val)}