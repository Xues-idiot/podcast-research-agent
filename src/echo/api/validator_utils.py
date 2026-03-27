"""验证工具API"""

from fastapi import APIRouter

from echo.research.validator_utils import get_validator_utils


router = APIRouter(prefix="/api/validate", tags=["validate"])


@router.post("/email")
async def is_email(value: str):
    return {"valid": get_validator_utils().is_email(value)}


@router.post("/url")
async def is_url(value: str):
    return {"valid": get_validator_utils().is_url(value)}


@router.post("/phone")
async def is_phone(value: str):
    return {"valid": get_validator_utils().is_phone(value)}


@router.post("/id_card")
async def is_id_card(value: str):
    return {"valid": get_validator_utils().is_id_card(value)}