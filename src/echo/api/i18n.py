"""国际化API - 多语言支持"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from echo.research.i18n import get_i18n_manager


router = APIRouter(prefix="/api/i18n", tags=["i18n"])


class SetLanguageRequest(BaseModel):
    """设置语言请求"""
    lang: str


class AddTranslationRequest(BaseModel):
    """添加翻译请求"""
    key: str
    lang: str
    text: str


@router.get("/languages")
async def get_languages():
    """获取支持的语言列表

    Returns:
        语言列表
    """
    manager = get_i18n_manager()
    return {"languages": manager.get_languages()}


@router.get("/current")
async def get_current_language():
    """获取当前语言

    Returns:
        当前语言
    """
    manager = get_i18n_manager()
    return {"lang": manager.get_language()}


@router.post("/current")
async def set_language(request: SetLanguageRequest):
    """设置当前语言

    Args:
        request: 语言代码

    Returns:
        操作结果
    """
    manager = get_i18n_manager()
    if not manager.set_language(request.lang):
        raise HTTPException(status_code=400, detail=f"Unsupported language: {request.lang}")
    return {"status": "changed", "lang": request.lang}


@router.get("/translate/{key}")
async def translate(key: str, lang: Optional[str] = None):
    """翻译单个键

    Args:
        key: 翻译键
        lang: 目标语言

    Returns:
        翻译文本
    """
    manager = get_i18n_manager()
    return {"key": key, "text": manager.t(key, lang)}


@router.get("/translate")
async def translate_all(lang: Optional[str] = None):
    """获取所有翻译

    Args:
        lang: 语言筛选

    Returns:
        翻译字典
    """
    manager = get_i18n_manager()
    return {"translations": manager.get_all_translations(lang)}


@router.post("/translations")
async def add_translation(request: AddTranslationRequest):
    """添加用户翻译

    Args:
        request: 翻译信息

    Returns:
        操作结果
    """
    manager = get_i18n_manager()
    manager.add_translation(request.key, request.lang, request.text)
    return {"status": "added", "key": request.key, "lang": request.lang}


@router.delete("/translations/{key}")
def remove_translation(key: str, lang: Optional[str] = None):
    """移除用户翻译

    Args:
        key: 翻译键
        lang: 语言，为空则移除整个键

    Returns:
        操作结果
    """
    manager = get_i18n_manager()
    manager.remove_translation(key, lang)
    return {"status": "removed", "key": key}


@router.post("/translate")
async def translate_template(key: str, params: dict, lang: Optional[str] = None):
    """带参数翻译

    Args:
        key: 翻译键
        params: 参数
        lang: 目标语言

    Returns:
        翻译文本
    """
    manager = get_i18n_manager()
    return {"key": key, "text": manager.tpl(key, params, lang)}
