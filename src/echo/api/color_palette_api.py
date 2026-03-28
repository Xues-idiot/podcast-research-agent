"""调色板生成API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.color_palette import get_color_palette_tool


router = APIRouter(prefix="/api/color-palette", tags=["color-palette"])


class PaletteRequest(BaseModel):
    hex_color: str


@router.post("/analogous")
async def analogous(request: PaletteRequest):
    tool = get_color_palette_tool()
    return {"result": tool.generate_analogous(request.hex_color)}


@router.post("/complementary")
async def complementary(request: PaletteRequest):
    tool = get_color_palette_tool()
    return {"result": tool.generate_complementary(request.hex_color)}