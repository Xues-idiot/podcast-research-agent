"""字符串哈希API"""

from fastapi import APIRouter
from pydantic import BaseModel

from echo.research.hash_string import get_hash_string_tool


router = APIRouter(prefix="/api/hash-string", tags=["hash-string"])


class HashRequest(BaseModel):
    text: str


@router.post("/md5")
async def md5(request: HashRequest):
    tool = get_hash_string_tool()
    return {"result": tool.md5(request.text)}


@router.post("/sha1")
async def sha1(request: HashRequest):
    tool = get_hash_string_tool()
    return {"result": tool.sha1(request.text)}


@router.post("/sha256")
async def sha256(request: HashRequest):
    tool = get_hash_string_tool()
    return {"result": tool.sha256(request.text)}


@router.post("/sha512")
async def sha512(request: HashRequest):
    tool = get_hash_string_tool()
    return {"result": tool.sha512(request.text)}


@router.post("/crc32")
async def crc32(request: HashRequest):
    tool = get_hash_string_tool()
    return {"result": tool.crc32(request.text)}


class MurmurRequest(BaseModel):
    text: str
    seed: int = 0


@router.post("/murmurhash")
async def murmurhash(request: MurmurRequest):
    tool = get_hash_string_tool()
    return {"result": tool.murmurhash(request.text, request.seed)}