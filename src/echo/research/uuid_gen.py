"""UUID工具"""

from typing import Optional
import uuid


class UuidGen:
    _instance: Optional["UuidGen"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def generate(self) -> str:
        return str(uuid.uuid4())

    def validate(self, text: str) -> bool:
        try:
            uuid.UUID(text)
            return True
        except:
            return False


def get_uuid_gen() -> UuidGen:
    return UuidGen()
