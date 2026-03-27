"""大小写转换API"""

from fastapi import APIRouter

from echo.research.case_converter import get_case_converter


router = APIRouter(prefix="/api/case", tags=["case"])


@router.post("/upper")
async def to_uppercase(text: str):
    return {"result": get_case_converter().to_uppercase(text)}


@router.post("/lower")
async def to_lowercase(text: str):
    return {"result": get_case_converter().to_lowercase(text)}


@router.post("/title")
async def to_title_case(text: str):
    return {"result": get_case_converter().to_title_case(text)}


@router.post("/sentence")
async def to_sentence_case(text: str):
    return {"result": get_case_converter().to_sentence_case(text)}


@router.post("/camel")
async def to_camel_case(text: str):
    return {"result": get_case_converter().to_camel_case(text)}


@router.post("/pascal")
async def to_pascal_case(text: str):
    return {"result": get_case_converter().to_pascal_case(text)}


@router.post("/snake")
async def to_snake_case(text: str):
    return {"result": get_case_converter().to_snake_case(text)}


@router.post("/kebab")
async def to_kebab_case(text: str):
    return {"result": get_case_converter().to_kebab_case(text)}