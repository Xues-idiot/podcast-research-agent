"""CSS颜色解析API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.css_parser import get_css_parser_tool


router = APIRouter(prefix="/api/css-parser", tags=["css-parser"])


class ParseRequest(BaseModel):
    css_color: str


@router.post("/parse")
async def parse(request: ParseRequest):
    tool = get_css_parser_tool()
    rgb = tool.parse(request.css_color)
    if rgb:
        return {"rgb": rgb, "hex": f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"}
    return {"error": "Invalid CSS color"}