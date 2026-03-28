"""单词提取工具"""

import re
from typing import List, Optional


class WordExtractTool:
    _instance: Optional["WordExtractTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def extract_words(self, text: str) -> List[str]:
        return re.findall(r'\b[a-zA-Z]+\b', text)

    def extract_unique_words(self, text: str) -> List[str]:
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return list(dict.fromkeys(words))

    def word_count(self, text: str) -> int:
        return len(re.findall(r'\b[a-zA-Z]+\b', text))


def get_word_extract_tool() -> WordExtractTool:
    return WordExtractTool()