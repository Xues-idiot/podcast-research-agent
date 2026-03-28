"""验证工具API路由"""
from fastapi import APIRouter
from pydantic import BaseModel
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from research.validator_utils import validate_email, validate_url, validate_phone, validate_json, validate_number


class ValidateRequest(BaseModel):
    value: str


router = APIRouter(prefix="/api/validate", tags=["validation"])


@router.post("/email")
async def email(request: ValidateRequest) -> dict:
    result = validate_email(request.value)
    return {"valid": result.valid, "message": result.message}


@router.post("/url")
async def url(request: ValidateRequest) -> dict:
    result = validate_url(request.value)
    return {"valid": result.valid, "message": result.message}


@router.post("/phone")
async def phone(request: ValidateRequest) -> dict:
    result = validate_phone(request.value)
    return {"valid": result.valid, "message": result.message}


@router.post("/json")
async def json_validate(request: ValidateRequest) -> dict:
    result = validate_json(request.value)
    return {"valid": result.valid, "message": result.message}


@router.post("/number")
async def number(request: ValidateRequest) -> dict:
    result = validate_number(request.value)
    return {"valid": result.valid, "message": result.message}
