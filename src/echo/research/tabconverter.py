"""制表符转换工具"""

from typing import Optional


class TabConverter:
    """制表符转换工具"""

    def spaces_to_tabs(self, text: str, tab_width: int = 4) -> str:
        """空格转制表符"""
        lines = text.split("\n")
        result = []
        for line in lines:
            result.append(line.replace(" " * tab_width, "\t"))
        return "\n".join(result)

    def tabs_to_spaces(self, text: str, tab_width: int = 4) -> str:
        """制表符转空格"""
        return text.expandtabs(tab_width)


_converter: Optional[TabConverter] = None


def get_tab_converter() -> TabConverter:
    global _converter
    if _converter is None:
        _converter = TabConverter()
    return _converter