"""翻译API"""

from fastapi import APIRouter

from echo.research.text_translator import get_text_translator


router = APIRouter(prefix="/api/translate", tags=["translate"])


@router.post("/translate")
async def translate_text(text: str, from_lang: str = "auto", to_lang: str = "en"):
    return {"result": get_text_translator().translate(text, from_lang, to_lang)}