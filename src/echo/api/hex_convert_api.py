"""十六进制API"""

from fastapi import APIRouter

from echo.research.hex_convert import get_hex_convert


router = APIRouter(prefix="/api/hex", tags=["hex"])


@router.post("/to-hex")
async def to_hex(data: str):
    """转十六进制"""
    tool = get_hex_convert()
    return {"result": tool.to_hex(data.encode())}


@router.post("/from-hex")
async def from_hex(hex_str: str):
    """从十六进制转"""
    tool = get_hex_convert()
    return {"result": tool.from_hex(hex_str).decode()}
