"""文本验证API"""

from fastapi import APIRouter

from echo.research.validator import get_text_validator


router = APIRouter(prefix="/api/validate", tags=["validate"])


@router.post("/length")
async def validate_length(text: str, min_length: int = 0, max_length: int = 100000):
    validator = get_text_validator()
    result = validator.validate_length(text, min_length, max_length)
    return {"is_valid": result.is_valid, "errors": result.errors}


@router.post("/encoding")
async def validate_encoding(text: str):
    validator = get_text_validator()
    result = validator.validate_encoding(text)
    return {"is_valid": result.is_valid, "errors": result.errors}


@router.post("/full")
async def full_validation(text: str):
    validator = get_text_validator()
    result = validator.full_validation(text)
    return {
        "is_valid": result.is_valid,
        "errors": result.errors,
        "warnings": result.warnings
    }