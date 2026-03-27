"""验证器工具"""

from typing import Optional, Callable, Any


class ValidatorTool:
    """验证器工具"""

    def validate(self, value: Any, rules: list) -> tuple:
        """验证值"""
        errors = []
        for rule in rules:
            if not rule(value):
                errors.append(f"Validation failed for {value}")
        return (len(errors) == 0, errors)


_tool: Optional[ValidatorTool] = None


def get_validator_tool() -> ValidatorTool:
    global _tool
    if _tool is None:
        _tool = ValidatorTool()
    return _tool