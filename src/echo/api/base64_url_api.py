"""Base64 URL安全编码API"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict

from echo.research.base64_url import get_base64_url_tool


router = APIRouter(prefix="/api/base64-url", tags=["base64-url"])


class EncodeRequest(BaseModel):
    text: str


@router.post("/encode")
async def encode(request: EncodeRequest):
    tool = get_base64_url_tool()
    return {"result": tool.encode(request.text)}


@router.post("/decode")
async def decode(request: EncodeRequest):
    tool = get_base64_url_tool()
    return {"result": tool.decode(request.text)}


@router.post("/encode-json")
async def encode_json(request: Dict[str, Any]):
    tool = get_base64_url_tool()
    return {"result": tool.encode_json(request)}


@router.post("/decode-json")
async def decode_json(request: EncodeRequest):
    tool = get_base64_url_tool()
    return {"result": tool.decode_json(request.text)}