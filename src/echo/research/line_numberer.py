"""行号添加工具"""

from typing import Optional


class LineNumberer:
    """行号添加工具"""

    def add_line_numbers(self, text: str, start: int = 1, format_str: str = "{num}: {line}", zero_pad: int = 0) -> str:
        """添加行号"""
        lines = text.split("\n")
        numbered = []
        for i, line in enumerate(lines, start=start):
            if zero_pad > 0:
                num_str = str(i).zfill(zero_pad)
            else:
                num_str = str(i)
            numbered.append(format_str.replace("{num}", num_str).replace("{line}", line))
        return "\n".join(numbered)

    def remove_line_numbers(self, text: str) -> str:
        """移除行号"""
        import re
        lines = text.split("\n")
        result = []
        for line in lines:
            cleaned = re.sub(r'^\d+[\s:.\t]+', '', line)
            result.append(cleaned)
        return "\n".join(result)


_numberer: Optional[LineNumberer] = None


def get_line_numberer() -> LineNumberer:
    global _numberer
    if _numberer is None:
        _numberer = LineNumberer()
    return _numberer