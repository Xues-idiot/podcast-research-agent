"""标点符号工具"""

from typing import Optional


class Punctuator:
    _instance: Optional["Punctuator"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_punctuation(self, text: str) -> str:
        sentences = text.split(".")
        result = []
        for i, sent in enumerate(sentences):
            sent = sent.strip()
            if sent and i < len(sentences) - 1:
                sent = sent[0].upper() + sent[1:] if sent else sent
                result.append(sent + ".")
        return " ".join(result)


def get_punctuator() -> Punctuator:
    return Punctuator()
