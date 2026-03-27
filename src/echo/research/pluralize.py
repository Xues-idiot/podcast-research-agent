"""复数化工具"""

from typing import Optional


class Pluralize:
    _instance: Optional["Pluralize"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def pluralize(self, word: str, count: int) -> str:
        if count == 1:
            return word
        rules = [
            ("(quiz)$", r"\1zes"),
            ("(matr|vert|ind)ix$", r"\1ices"),
            ("(ax|test)is$", r"\1es"),
            ("([^aeiouy])$", r"\1s"),
            ("([^aeiouy]y)$", r"\1ies"),
            ("(h|x)$", r"\1es"),
            ("$", "s")
        ]
        import re
        for pattern, replacement in rules:
            if re.search(pattern, word):
                return re.sub(pattern, replacement, word)
        return word


def get_pluralize() -> Pluralize:
    return Pluralize()
