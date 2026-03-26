"""文本差异工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class DiffResult:
    """差异结果"""
    operation: str  # add, remove, equal
    text: str


class TextDiff:
    """文本差异比较"""

    def diff(self, text1: str, text2: str) -> list[DiffResult]:
        """计算文本差异"""
        if text1 == text2:
            return [DiffResult(operation="equal", text=text1)]

        lines1 = text1.split("\n")
        lines2 = text2.split("\n")

        result = []
        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            l1 = lines1[i] if i < len(lines1) else ""
            l2 = lines2[i] if i < len(lines2) else ""

            if l1 == l2:
                result.append(DiffResult(operation="equal", text=l1))
            else:
                if l1:
                    result.append(DiffResult(operation="remove", text=l1))
                if l2:
                    result.append(DiffResult(operation="add", text=l2))

        return result

    def diff_summary(self, text1: str, text2: str) -> dict:
        """差异摘要"""
        diffs = self.diff(text1, text2)
        added = sum(1 for d in diffs if d.operation == "add")
        removed = sum(1 for d in diffs if d.operation == "remove")
        equal = sum(1 for d in diffs if d.operation == "equal")

        return {
            "lines_added": added,
            "lines_removed": removed,
            "lines_unchanged": equal,
            "total_changes": added + removed,
        }


_comparer: Optional[TextDiff] = None


def get_text_diff() -> TextDiff:
    global _comparer
    if _comparer is None:
        _comparer = TextDiff()
    return _comparer