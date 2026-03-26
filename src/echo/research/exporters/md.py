"""Markdown格式化工具"""

from typing import Optional


class MarkdownFormatter:
    """Markdown格式化器"""

    @staticmethod
    def format_header(text: str, level: int = 1) -> str:
        return f"{'#' * level} {text}\n\n"

    @staticmethod
    def format_bold(text: str) -> str:
        return f"**{text}**"

    @staticmethod
    def format_italic(text: str) -> str:
        return f"*{text}*"

    @staticmethod
    def format_link(text: str, url: str) -> str:
        return f"[{text}]({url})"

    @staticmethod
    def format_list_item(text: str, ordered: bool = False, index: int = 1) -> str:
        prefix = f"{index}." if ordered else "-"
        return f"{prefix} {text}\n"

    @staticmethod
    def format_code_block(code: str, language: str = "") -> str:
        return f"```{language}\n{code}\n```\n"

    @staticmethod
    def format_quote(text: str) -> str:
        return f"> {text}\n"

    @staticmethod
    def format_table(headers: list, rows: list) -> str:
        lines = []
        # 表头
        lines.append("| " + " | ".join(headers) + " |")
        # 分隔符
        lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
        # 数据行
        for row in rows:
            lines.append("| " + " | ".join(str(cell) for cell in row) + " |")
        return "\n".join(lines) + "\n"

    @staticmethod
    def format_keypoints(keypoints: list, include_importance: bool = True) -> str:
        lines = []
        for i, kp in enumerate(keypoints, 1):
            content = kp.get("content", kp) if isinstance(kp, dict) else kp
            lines.append(f"{i}. {content}")
            if include_importance and isinstance(kp, dict):
                importance = kp.get("importance", "")
                if importance:
                    lines.append(f"   - 重要性: {importance}")
        return "\n".join(lines) + "\n\n"


_formatter: Optional[MarkdownFormatter] = None

def get_markdown_formatter() -> MarkdownFormatter:
    global _formatter
    if _formatter is None:
        _formatter = MarkdownFormatter()
    return _formatter
