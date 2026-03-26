"""文本验证工具"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    errors: list[str]
    warnings: list[str]


class TextValidator:
    """文本验证工具"""

    def validate_length(self, text: str, min_length: int = 0, max_length: int = 100000) -> ValidationResult:
        """验证长度"""
        errors = []
        warnings = []
        length = len(text)

        if min_length > 0 and length < min_length:
            errors.append(f"文本长度({length})低于最小要求({min_length})")
        if length > max_length:
            errors.append(f"文本长度({length})超过最大限制({max_length})")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def validate_encoding(self, text: str) -> ValidationResult:
        """验证编码"""
        errors = []
        warnings = []

        try:
            text.encode('utf-8')
        except UnicodeEncodeError:
            errors.append("文本包含无法用UTF-8编码的字符")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def validate_no_nulls(self, text: str) -> ValidationResult:
        """验证无空字符"""
        errors = []
        warnings = []

        if '\x00' in text:
            errors.append("文本包含空字符(NULL)")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def validate_structure(self, text: str, expect_paragraphs: bool = False) -> ValidationResult:
        """验证结构"""
        errors = []
        warnings = []

        lines = text.split("\n")
        empty_lines = sum(1 for l in lines if not l.strip())

        if expect_paragraphs and empty_lines == 0:
            warnings.append("文本似乎没有段落分隔")

        if len(lines) > 10000:
            warnings.append("文本行数过多，可能需要分段处理")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )

    def full_validation(self, text: str) -> ValidationResult:
        """完整验证"""
        all_errors = []
        all_warnings = []

        all_errors.extend(self.validate_length(text).errors)
        all_errors.extend(self.validate_encoding(text).errors)
        all_errors.extend(self.validate_no_nulls(text).errors)
        all_warnings.extend(self.validate_structure(text).warnings)

        return ValidationResult(
            is_valid=len(all_errors) == 0,
            errors=all_errors,
            warnings=all_warnings
        )


_validator: Optional[TextValidator] = None


def get_text_validator() -> TextValidator:
    global _validator
    if _validator is None:
        _validator = TextValidator()
    return _validator