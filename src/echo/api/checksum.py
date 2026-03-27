"""校验和API"""

from fastapi import APIRouter

from echo.research.checksum import get_checksum_tool


router = APIRouter(prefix="/api/checksum", tags=["checksum"])


@router.post("/md5")
async def md5(data: str):
    return {"checksum": get_checksum_tool().md5(data)}


@router.post("/sha256")
async def sha256(data: str):
    return {"checksum": get_checksum_tool().sha256(data)}


@router.post("/crc32")
async def crc32(data: str):
    return {"checksum": get_checksum_tool().crc32(data)}