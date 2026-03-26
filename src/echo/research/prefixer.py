"""文本前缀工具"""

from typing import Optional


class TextPrefixer:
    """文本前缀添加工具"""

    def add_line_numbers(self, text: str, start: int = 1, format_str: str = "{num}: {line}") -> str:
        """添加行号"""
        lines = text.split("\n")
        numbered = []
        for i, line in enumerate(lines, start=start):
            numbered.append(format_str.format(num=i, line=line))
        return "\n".join(numbered)

    def add_bullet_points(self, text: str, bullet: str = "-") -> str:
        """添加项目符号"""
        lines = text.split("\n")
        bulleted = []
        for line in lines:
            line = line.strip()
            if line:
                bulleted.append(f"{bullet} {line}")
            else:
                bulleted.append("")
        return "\n".join(bulleted)

    def add_timestamp_prefix(self, text: str, prefix: str = "[00:00] ") -> str:
        """添加时间戳前缀"""
        lines = text.split("\n")
        return "\n".join(f"{prefix}{line}" if line.strip() else "" for line in lines)

    def add_header_line(self, text: str, header: str = "=", width: int = 80) -> str:
        """添加标题行"""
        separator = header * width
        return f"{separator}\n{text}\n{separator}"


_prefixer: Optional[TextPrefixer] = None


def get_text_prefixer() -> TextPrefixer:
    global _prefixer
    if _prefixer is None:
        _prefixer = TextPrefixer()
    return _prefixer