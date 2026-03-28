"""颜色工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.color_utils import hex_to_rgb, rgb_to_hex, rgb_to_hsl, hsl_to_rgb, lighten, darken


class HexRequest(BaseModel):
    hex_color: str


class RGBRequest(BaseModel):
    r: int
    g: int
    b: int


class LightenRequest(BaseModel):
    hex_color: str
    amount: float = 0.2


router = APIRouter(prefix="/api/color", tags=["color"])


@router.post("/hex-to-rgb")
async def hex_to_rgb_endpoint(request: HexRequest) -> dict:
    r, g, b = hex_to_rgb(request.hex_color)
    return {"r": r, "g": g, "b": b}


@router.post("/rgb-to-hex")
async def rgb_to_hex_endpoint(request: RGBRequest) -> dict:
    return {"hex": rgb_to_hex(request.r, request.g, request.b)}


@router.post("/rgb-to-hsl")
async def rgb_to_hsl_endpoint(request: RGBRequest) -> dict:
    h, s, l = rgb_to_hsl(request.r, request.g, request.b)
    return {"h": h, "s": s, "l": l}


@router.post("/hsl-to-rgb")
async def hsl_to_rgb_endpoint(request: RGBRequest) -> dict:
    r, g, b = hsl_to_rgb(request.r, request.g, request.b)
    return {"r": r, "g": g, "b": b}


@router.post("/lighten")
async def lighten_endpoint(request: LightenRequest) -> dict:
    return {"hex": lighten(request.hex_color, request.amount)}


@router.post("/darken")
async def darken_endpoint(request: LightenRequest) -> dict:
    return {"hex": darken(request.hex_color, request.amount)}
