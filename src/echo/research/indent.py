"""缩进工具"""

from typing import Optional


class IndentTool:
    _instance: Optional["IndentTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def indent(self, text: str, spaces: int = 4) -> str:
        indent_str = " " * spaces
        return "\n".join(indent_str + line for line in text.split("\n"))

    def unindent(self, text: str, spaces: int = 4) -> str:
        indent_str = " " * spaces
        return "\n".join(line[len(indent_str):] if line.startswith(indent_str) else line for line in text.split("\n"))


def get_indent_tool() -> IndentTool:
    return IndentTool()
