"""正则表达式工具"""
import re
from typing import List, Optional


def regex_match(pattern: str, text: str) -> bool:
    return bool(re.match(pattern, text))


def regex_search(pattern: str, text: str) -> Optional[str]:
    match = re.search(pattern, text)
    return match.group() if match else None


def regex_find_all(pattern: str, text: str) -> List[str]:
    return re.findall(pattern, text)


def regex_replace(pattern: str, text: str, replacement: str) -> str:
    return re.sub(pattern, replacement, text)


def regex_split(pattern: str, text: str) -> List[str]:
    return re.split(pattern, text)


def regex_groups(pattern: str, text: str) -> Optional[tuple]:
    match = re.search(pattern, text)
    return match.groups() if match else None


def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))


def is_valid_url(url: str) -> bool:
    pattern = r'^https?://[\w\.-]+\.\w+'
    return bool(re.match(pattern, url))


def extract_numbers(text: str) -> List[str]:
    return re.findall(r'-?\d+\.?\d*', text)


def extract_emails(text: str) -> List[str]:
    return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
