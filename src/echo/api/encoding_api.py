"""编码转换API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.encoding_utils import encode_base64, decode_base64, encode_url, decode_url, encode_json, decode_json, encode_hex, decode_hex


class EncodeRequest(BaseModel):
    value: str


router = APIRouter(prefix="/api/encode", tags=["encoding"])


@router.post("/base64")
async def base64_encode(request: EncodeRequest) -> dict:
    result = encode_base64(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/base64-decode")
async def base64_decode(request: EncodeRequest) -> dict:
    result = decode_base64(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/url")
async def url_encode(request: EncodeRequest) -> dict:
    result = encode_url(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/url-decode")
async def url_decode(request: EncodeRequest) -> dict:
    result = decode_url(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/json")
async def json_encode(request: EncodeRequest) -> dict:
    result = encode_json(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/json-decode")
async def json_decode(request: EncodeRequest) -> dict:
    result = decode_json(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/hex")
async def hex_encode(request: EncodeRequest) -> dict:
    result = encode_hex(request.value)
    return {"result": result.result, "success": result.success}


@router.post("/hex-decode")
async def hex_decode(request: EncodeRequest) -> dict:
    result = decode_hex(request.value)
    return {"result": result.result, "success": result.success}
