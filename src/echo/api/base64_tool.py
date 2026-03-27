"""Base64工具API"""

from fastapi import APIRouter

from echo.research.base64_tool import get_base64_tool


router = APIRouter(prefix="/api/base64", tags=["base64"])


@router.post("/encode")
async def encode(data: str):
    return {"result": get_base64_tool().encode(data)}


@router.post("/decode")
async def decode(encoded: str):
    return {"result": get_base64_tool().decode(encoded)}


@router.post("/encode_url")
async def encode_url(data: str):
    return {"result": get_base64_tool().encode_url(data)}


@router.post("/decode_url")
async def decode_url(encoded: str):
    return {"result": get_base64_tool().decode_url(encoded)}