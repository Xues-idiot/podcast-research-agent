"""符号API"""

from fastapi import APIRouter

from echo.research.sign_tool import get_sign_tool


router = APIRouter(prefix="/api/sign", tags=["sign"])


@router.post("/sign")
async def sign(value: float):
    return {"result": get_sign_tool().sign(value)}


@router.post("/is-positive")
async def is_positive(value: float):
    return {"result": get_sign_tool().is_positive(value)}


@router.post("/is-negative")
async def is_negative(value: float):
    return {"result": get_sign_tool().is_negative(value)}


@router.post("/abs")
async def abs_value(value: float):
    return {"result": get_sign_tool().abs_value(value)}