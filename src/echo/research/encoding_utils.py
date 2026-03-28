"""编码转换工具"""
import base64
import urllib.parse
import json
from dataclasses import dataclass


@dataclass
class EncodeResult:
    result: str
    success: bool


def encode_base64(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=base64.b64encode(s.encode()).decode(), success=True)
    except:
        return EncodeResult(result="", success=False)


def decode_base64(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=base64.b64decode(s.encode()).decode(), success=True)
    except:
        return EncodeResult(result="", success=False)


def encode_url(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=urllib.parse.quote(s), success=True)
    except:
        return EncodeResult(result="", success=False)


def decode_url(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=urllib.parse.unquote(s), success=True)
    except:
        return EncodeResult(result="", success=False)


def encode_json(obj: dict) -> EncodeResult:
    try:
        return EncodeResult(result=json.dumps(obj), success=True)
    except:
        return EncodeResult(result="", success=False)


def decode_json(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=json.loads(s), success=True)
    except:
        return EncodeResult(result="", success=False)


def encode_hex(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=s.encode().hex(), success=True)
    except:
        return EncodeResult(result="", success=False)


def decode_hex(s: str) -> EncodeResult:
    try:
        return EncodeResult(result=bytes.fromhex(s).decode(), success=True)
    except:
        return EncodeResult(result="", success=False)
