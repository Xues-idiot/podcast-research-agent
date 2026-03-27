"""文本哈希API"""

from fastapi import APIRouter

from echo.research.text_hasher import get_text_hasher


router = APIRouter(prefix="/api/hash", tags=["hash"])


@router.post("/md5")
async def hash_md5(text: str):
    return {"result": get_text_hasher().hash_md5(text)}


@router.post("/sha256")
async def hash_sha256(text: str):
    return {"result": get_text_hasher().hash_sha256(text)}


@router.post("/sha1")
async def hash_sha1(text: str):
    return {"result": get_text_hasher().hash_sha1(text)}


@router.post("/sha512")
async def hash_sha512(text: str):
    return {"result": get_text_hasher().hash_sha512(text)}