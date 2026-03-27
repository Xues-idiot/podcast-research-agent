"""文本差异工具"""

from typing import List, Tuple


class TextDiff:
    _instance: Optional["TextDiff"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def diff_lines(self, text1: str, text2: str) -> List[Tuple[str, str]]:
        lines1 = text1.split("\n")
        lines2 = text2.split("\n")
        result = []
        max_len = max(len(lines1), len(lines2))
        for i in range(max_len):
            l1 = lines1[i] if i < len(lines1) else ""
            l2 = lines2[i] if i < len(lines2) else ""
            if l1 != l2:
                result.append((l1, l2))
        return result


def get_text_diff() -> TextDiff:
    return TextDiff()
