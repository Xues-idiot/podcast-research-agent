"""位运算API"""

from fastapi import APIRouter

from echo.research.bitwise_tool import get_bitwise_tool


router = APIRouter(prefix="/api/bitwise", tags=["bitwise"])


@router.post("/and")
async def and_(a: int, b: int):
    return {"result": get_bitwise_tool().and_(a, b)}


@router.post("/or")
async def or_(a: int, b: int):
    return {"result": get_bitwise_tool().or_(a, b)}


@router.post("/xor")
async def xor(a: int, b: int):
    return {"result": get_bitwise_tool().xor(a, b)}


@router.post("/shift-left")
async def shift_left(value: int, bits: int):
    return {"result": get_bitwise_tool().shift_left(value, bits)}


@router.post("/shift-right")
async def shift_right(value: int, bits: int):
    return {"result": get_bitwise_tool().shift_right(value, bits)}