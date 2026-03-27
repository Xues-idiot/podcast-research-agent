"""文件大小API"""

from fastapi import APIRouter

from echo.research.file_size import get_file_size_tool


router = APIRouter(prefix="/api/file_size", tags=["file_size"])


@router.post("/bytes_to_human")
async def bytes_to_human(bytes_count: int):
    return {"result": get_file_size_tool().bytes_to_human(bytes_count)}


@router.post("/human_to_bytes")
async def human_to_bytes(size_str: str):
    return {"result": get_file_size_tool().human_to_bytes(size_str)}