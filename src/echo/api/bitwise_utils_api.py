"""位运算工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.bitwise_utils import (
    bitwise_and, bitwise_or, bitwise_xor, bitwise_not,
    left_shift, right_shift, count_set_bits,
    get_bit, set_bit, clear_bit, toggle_bit,
    is_power_of_two, bit_length
)


class BinaryOpRequest(BaseModel):
    a: int
    b: int


class UnaryOpRequest(BaseModel):
    a: int


class BitPosRequest(BaseModel):
    a: int
    pos: int


router = APIRouter(prefix="/api/bitwise", tags=["bitwise"])


@router.post("/and")
async def bw_and(request: BinaryOpRequest) -> dict:
    return {"result": bitwise_and(request.a, request.b)}


@router.post("/or")
async def bw_or(request: BinaryOpRequest) -> dict:
    return {"result": bitwise_or(request.a, request.b)}


@router.post("/xor")
async def bw_xor(request: BinaryOpRequest) -> dict:
    return {"result": bitwise_xor(request.a, request.b)}


@router.post("/not")
async def bw_not(request: UnaryOpRequest) -> dict:
    return {"result": bitwise_not(request.a)}


@router.post("/left-shift")
async def bw_left_shift(request: BinaryOpRequest) -> dict:
    return {"result": left_shift(request.a, request.b)}


@router.post("/right-shift")
async def bw_right_shift(request: BinaryOpRequest) -> dict:
    return {"result": right_shift(request.a, request.b)}


@router.post("/count-bits")
async def bw_count_bits(request: UnaryOpRequest) -> dict:
    return {"result": count_set_bits(request.a)}


@router.post("/get-bit")
async def bw_get_bit(request: BitPosRequest) -> dict:
    return {"result": get_bit(request.a, request.pos)}


@router.post("/set-bit")
async def bw_set_bit(request: BitPosRequest) -> dict:
    return {"result": set_bit(request.a, request.pos)}


@router.post("/clear-bit")
async def bw_clear_bit(request: BitPosRequest) -> dict:
    return {"result": clear_bit(request.a, request.pos)}


@router.post("/toggle-bit")
async def bw_toggle_bit(request: BitPosRequest) -> dict:
    return {"result": toggle_bit(request.a, request.pos)}


@router.post("/is-power-of-two")
async def bw_is_power(request: UnaryOpRequest) -> dict:
    return {"result": is_power_of_two(request.a)}


@router.post("/bit-length")
async def bw_bit_length(request: UnaryOpRequest) -> dict:
    return {"result": bit_length(request.a)}