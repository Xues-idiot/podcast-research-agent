"""颜色API"""

from fastapi import APIRouter

from echo.research.color_tool import get_color_tool


router = APIRouter(prefix="/api/color", tags=["color"])


@router.post("/hex-to-rgb")
async def hex_to_rgb(hex_color: str):
    """HEX转RGB"""
    tool = get_color_tool()
    return {"rgb": tool.hex_to_rgb(hex_color)}


@router.post("/rgb-to-hex")
async def rgb_to_hex(r: int, g: int, b: int):
    """RGB转HEX"""
    tool = get_color_tool()
    return {"hex": tool.rgb_to_hex(r, g, b)}
