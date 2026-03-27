"""栈工具"""

from typing import Any, Optional


class StackTool:
    _instance: Optional["StackTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def push(self, stack: list, item: Any) -> None:
        stack.append(item)

    def pop(self, stack: list) -> Any:
        return stack.pop() if stack else None

    def peek(self, stack: list) -> Any:
        return stack[-1] if stack else None

    def size(self, stack: list) -> int:
        return len(stack)


def get_stack_tool() -> StackTool:
    return StackTool()
