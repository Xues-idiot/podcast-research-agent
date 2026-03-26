"""文本清理工具"""

import re
from typing import Optional


class TextCleaner:
    """文本清理工具"""

    def remove_extra_whitespace(self, text: str) -> str:
        """移除多余空白"""
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def remove_extra_newlines(self, text: str) -> str:
        """移除多余换行"""
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

    def remove_urls(self, text: str) -> str:
        """移除URL"""
        return re.sub(r'https?://\S+', '', text)

    def remove_emails(self, text: str) -> str:
        """移除邮箱"""
        return re.sub(r'\S+@\S+\.\S+', '', text)

    def remove_html_tags(self, text: str) -> str:
        """移除HTML标签"""
        return re.sub(r'<[^>]+>', '', text)

    def remove_special_chars(self, text: str, keep_chinese: bool = True) -> str:
        """移除特殊字符"""
        if keep_chinese:
            pattern = r'[^\w\s\u4e00-\u9fff,.!?;:\'\"-]'
        else:
            pattern = r'[^\w\s,.!?;:\'\"-]'
        return re.sub(pattern, '', text)

    def normalize_punctuation(self, text: str) -> str:
        """规范化标点"""
        # 统一引号
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace(''', "'").replace(''', "'")
        # 统一破折号
        text = text.replace('—', '-').replace('–', '-')
        return text

    def full_clean(self, text: str) -> str:
        """完整清理"""
        text = self.remove_html_tags(text)
        text = self.remove_urls(text)
        text = self.remove_emails(text)
        text = self.normalize_punctuation(text)
        text = self.remove_extra_newlines(text)
        text = self.remove_extra_whitespace(text)
        return text


_cleaner: Optional[TextCleaner] = None


def get_text_cleaner() -> TextCleaner:
    global _cleaner
    if _cleaner is None:
        _cleaner = TextCleaner()
    return _cleaner