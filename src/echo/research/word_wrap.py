"""单词换行工具"""

from typing import Optional


class WordWrap:
    _instance: Optional["WordWrap"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def wrap(self, text: str, width: int = 80) -> List[str]:
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) <= width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        return lines


def get_word_wrap() -> WordWrap:
    return WordWrap()
