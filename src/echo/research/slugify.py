"""Slugify工具"""

import re
from typing import Optional


class Slugify:
    _instance: Optional["Slugify"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def slugify(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[-\s]+", "-", text)
        return text.strip("-")


def get_slugify() -> Slugify:
    return Slugify()
