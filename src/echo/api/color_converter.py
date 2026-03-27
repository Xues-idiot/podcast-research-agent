"""颜色转换API"""

from fastapi import APIRouter

from echo.research.color_converter import get_color_converter


router = APIRouter(prefix="/api/color", tags=["color"])


@router.post("/hex_to_rgb")
async def hex_to_rgb(hex_color: str):
    return get_color_converter().hex_to_rgb(hex_color)


@router.post("/rgb_to_hex")
async def rgb_to_hex(r: int, g: int, b: int):
    return {"result": get_color_converter().rgb_to_hex(r, g, b)}


@router.post("/rgb_to_hsl")
async def rgb_to_hsl(r: int, g: int, b: int):
    return get_color_converter().rgb_to_hsl(r, g, b)