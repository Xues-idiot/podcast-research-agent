"""加密工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.crypto_utils import generate_token, generate_random_hex, generate_password, secure_random_int, generate_uuid, constant_time_compare, salt


class TokenRequest(BaseModel):
    length: int = 32


class PasswordRequest(BaseModel):
    length: int = 16
    chars: str = None


class RandomIntRequest(BaseModel):
    min_val: int = 0
    max_val: int = 100


class CompareRequest(BaseModel):
    a: str
    b: str


router = APIRouter(prefix="/api/crypto", tags=["crypto"])


@router.post("/token")
async def token(request: TokenRequest) -> dict:
    return {"result": generate_token(request.length)}


@router.post("/random-hex")
async def random_hex(request: TokenRequest) -> dict:
    return {"result": generate_random_hex(request.length)}


@router.post("/password")
async def password(request: PasswordRequest) -> dict:
    return {"result": generate_password(request.length, request.chars)}


@router.post("/random-int")
async def random_int(request: RandomIntRequest) -> dict:
    return {"result": secure_random_int(request.min_val, request.max_val)}


@router.post("/uuid")
async def uuid() -> dict:
    return {"result": generate_uuid()}


@router.post("/compare")
async def compare(request: CompareRequest) -> dict:
    return {"result": constant_time_compare(request.a, request.b)}


@router.post("/salt")
async def salt() -> dict:
    return {"result": salt()}
