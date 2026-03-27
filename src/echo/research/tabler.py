"""制表符转换工具"""

from typing import Optional


class TablerTool:
    """制表符转换工具"""

    def spaces_to_tabs(self, text: str, width: int = 4) -> str:
        """空格转制表符"""
        lines = text.split("\n")
        result = []
        for line in lines:
            result.append(line.replace(" " * width, "\t"))
        return "\n".join(result)

    def tabs_to_spaces(self, text: str, width: int = 4) -> str:
        """制表符转空格"""
        return text.replace("\t", " " * width)


_tabler_tool: Optional[TablerTool] = None


def get_tabler_tool() -> TablerTool:
    global _tabler_tool
    if _tabler_tool is None:
        _tabler_tool = TablerTool()
    return _tabler_tool