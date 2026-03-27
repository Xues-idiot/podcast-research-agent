"""验证器API"""

from fastapi import APIRouter

from echo.research.validator_tool import get_validator_tool


router = APIRouter(prefix="/api/validator", tags=["validator"])


@router.post("/validate")
async def validate(value, rules: list):
    return {"result": get_validator_tool().validate(value, rules)}


@router.post("/required")
async def required(value):
    return {"result": get_validator_tool().required(value)}