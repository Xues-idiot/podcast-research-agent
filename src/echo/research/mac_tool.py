"""MAC地址工具"""

from typing import Optional


class MacTool:
    _instance: Optional["MacTool"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_valid(self, mac: str) -> bool:
        mac = mac.replace(":", "").replace("-", "").upper()
        if len(mac) != 12:
            return False
        try:
            int(mac, 16)
            return True
        except:
            return False


def get_mac_tool() -> MacTool:
    return MacTool()
