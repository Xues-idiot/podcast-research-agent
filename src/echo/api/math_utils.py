"""数学工具API"""

from fastapi import APIRouter

from echo.research.math_utils import get_math_utils


router = APIRouter(prefix="/api/math", tags=["math"])


@router.post("/clamp")
async def clamp(value: float, min_val: float, max_val: float):
    return {"result": get_math_utils().clamp(value, min_val, max_val)}


@router.post("/lerp")
async def lerp(a: float, b: float, t: float):
    return {"result": get_math_utils().lerp(a, b, t)}


@router.post("/map_range")
async def map_range(value: float, in_min: float, in_max: float, out_min: float, out_max: float):
    return {"result": get_math_utils().map_range(value, in_min, in_max, out_min, out_max)}


@router.post("/gcd")
async def gcd(a: int, b: int):
    return {"result": get_math_utils().gcd(a, b)}


@router.post("/lcm")
async def lcm(a: int, b: int):
    return {"result": get_math_utils().lcm(a, b)}