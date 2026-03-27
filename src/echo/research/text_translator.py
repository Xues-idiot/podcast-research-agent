"""翻译工具"""

from typing import Optional


class TextTranslator:
    """翻译工具(占位,实际需要LLM或翻译API)"""

    def translate(self, text: str, from_lang: str = "auto", to_lang: str = "en") -> str:
        """翻译文本"""
        return f"[Translation from {from_lang} to {to_lang}]: {text}"


_translator: Optional[TextTranslator] = None


def get_text_translator() -> TextTranslator:
    global _translator
    if _translator is None:
        _translator = TextTranslator()
    return _translator