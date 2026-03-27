"""密码生成API"""

from fastapi import APIRouter

from echo.research.password_generator import get_password_generator


router = APIRouter(prefix="/api/password", tags=["password"])


@router.post("/generate")
async def generate_password(length: int = 16, include_special: bool = True):
    return {"password": get_password_generator().generate(length, include_special)}


@router.post("/strong")
async def generate_strong_password(length: int = 16):
    return {"password": get_password_generator().generate_strong(length)}