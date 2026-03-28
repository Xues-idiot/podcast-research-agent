"""哈希工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.hash_utils import md5, sha1, sha256, sha512, hash_any, verify_hash


class HashRequest(BaseModel):
    text: str


class VerifyRequest(BaseModel):
    text: str
    hash_value: str
    algo: str = "md5"


router = APIRouter(prefix="/api/hash", tags=["hash"])


@router.post("/md5")
async def md5_hash(request: HashRequest) -> dict:
    return {"result": md5(request.text)}


@router.post("/sha1")
async def sha1_hash(request: HashRequest) -> dict:
    return {"result": sha1(request.text)}


@router.post("/sha256")
async def sha256_hash(request: HashRequest) -> dict:
    return {"result": sha256(request.text)}


@router.post("/sha512")
async def sha512_hash(request: HashRequest) -> dict:
    return {"result": sha512(request.text)}


@router.post("/any")
async def any_hash(request: HashRequest) -> dict:
    return {"result": hash_any(request.text)}


@router.post("/verify")
async def verify(request: VerifyRequest) -> dict:
    return {"result": verify_hash(request.text, request.hash_value, request.algo)}
