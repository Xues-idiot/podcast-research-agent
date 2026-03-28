"""验证工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Optional
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.validate_utils import (
    is_valid_email, is_valid_url, is_valid_phone, is_valid_ip,
    is_valid_cidr, is_valid_hex_color, is_valid_credit_card,
    is_valid_uuid, is_valid_json, validate_range, validate_length
)


class StringRequest(BaseModel):
    value: str


class PhoneRequest(BaseModel):
    phone: str
    country: str = "CN"


class IPRequest(BaseModel):
    ip: str
    version: int = 4


class CIDRRequest(BaseModel):
    cidr: str


class ColorRequest(BaseModel):
    color: str


class CardRequest(BaseModel):
    card: str


class UUIDRequest(BaseModel):
    uuid: str


class JSONRequest(BaseModel):
    text: str


class RangeRequest(BaseModel):
    value: float
    min_val: float
    max_val: float


class LengthRequest(BaseModel):
    text: str
    min_len: int = 0
    max_len: Optional[int] = None


router = APIRouter(prefix="/api/validate", tags=["validate"])


@router.post("/email")
async def validate_email(request: StringRequest) -> dict:
    return {"result": is_valid_email(request.value)}


@router.post("/url")
async def validate_url(request: StringRequest) -> dict:
    return {"result": is_valid_url(request.value)}


@router.post("/phone")
async def validate_phone(request: PhoneRequest) -> dict:
    return {"result": is_valid_phone(request.phone, request.country)}


@router.post("/ip")
async def validate_ip(request: IPRequest) -> dict:
    return {"result": is_valid_ip(request.ip, request.version)}


@router.post("/cidr")
async def validate_cidr(request: CIDRRequest) -> dict:
    return {"result": is_valid_cidr(request.cidr)}


@router.post("/hex-color")
async def validate_color(request: ColorRequest) -> dict:
    return {"result": is_valid_hex_color(request.color)}


@router.post("/credit-card")
async def validate_card(request: CardRequest) -> dict:
    return {"result": is_valid_credit_card(request.card)}


@router.post("/uuid")
async def validate_uuid(request: UUIDRequest) -> dict:
    return {"result": is_valid_uuid(request.uuid)}


@router.post("/json")
async def validate_json(request: JSONRequest) -> dict:
    return {"result": is_valid_json(request.text)}


@router.post("/range")
async def validate_range(request: RangeRequest) -> dict:
    return {"result": validate_range(request.value, request.min_val, request.max_val)}


@router.post("/length")
async def validate_length(request: LengthRequest) -> dict:
    return {"result": validate_length(request.text, request.min_len, request.max_len)}