"""验证工具集合"""
import re
from dataclasses import dataclass


@dataclass
class ValidationResult:
    valid: bool
    message: str


def validate_email(email: str) -> ValidationResult:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return ValidationResult(valid=True, message="Valid email")
    return ValidationResult(valid=False, message="Invalid email format")


def validate_url(url: str) -> ValidationResult:
    pattern = r'^https?://'
    if re.match(pattern, url):
        return ValidationResult(valid=True, message="Valid URL")
    return ValidationResult(valid=False, message="Invalid URL format")


def validate_phone(phone: str) -> ValidationResult:
    pattern = r'^1[3-9]\d{9}$'
    if re.match(pattern, phone):
        return ValidationResult(valid=True, message="Valid phone")
    return ValidationResult(valid=False, message="Invalid phone format")


def validate_json(s: str) -> ValidationResult:
    import json
    try:
        json.loads(s)
        return ValidationResult(valid=True, message="Valid JSON")
    except:
        return ValidationResult(valid=False, message="Invalid JSON format")


def validate_number(s: str) -> ValidationResult:
    try:
        float(s)
        return ValidationResult(valid=True, message="Valid number")
    except:
        return ValidationResult(valid=False, message="Invalid number format")
