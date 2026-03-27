"""文本编码API"""

from fastapi import APIRouter

from echo.research.text_encoder import get_text_encoder


router = APIRouter(prefix="/api/encode", tags=["encode"])


@router.post("/base64")
async def encode_base64(text: str):
    encoder = get_text_encoder()
    return {"result": encoder.to_base64(text)}


@router.post("/base64/decode")
async def decode_base64(encoded: str):
    encoder = get_text_encoder()
    return {"result": encoder.from_base64(encoded)}


@router.post("/hex")
async def encode_hex(text: str):
    encoder = get_text_encoder()
    return {"result": encoder.to_hex(text)}


@router.post("/hex/decode")
async def decode_hex(hex_str: str):
    encoder = get_text_encoder()
    return {"result": encoder.from_hex(hex_str)}


@router.post("/url")
async def encode_url(text: str):
    encoder = get_text_encoder()
    return {"result": encoder.to_url_encode(text)}


@router.post("/url/decode")
async def decode_url(encoded: str):
    encoder = get_text_encoder()
    return {"result": encoder.from_url_encode(encoded)}