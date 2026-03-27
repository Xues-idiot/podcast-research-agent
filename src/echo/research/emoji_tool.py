"""表情符号工具"""

from typing import Optional


class EmojiTool:
    """表情符号工具"""

    EMOJI_MAP = {
        "happy": ["😀", "😃", "😄", "😁", "😊"],
        "sad": ["😢", "😭", "😞", "😔"],
        "angry": ["😠", "😡", "🤬"],
        "love": ["❤️", "💕", "😍", "🥰"],
        "laugh": ["😂", "🤣", "😆"],
        "surprise": ["😮", "😲", "🙀"],
        "think": ["🤔", "💭"],
        "ok": ["👌", "✅", "👍"],
    }

    def random_emoji(self, category: str = "happy") -> str:
        """获取随机表情"""
        emojis = self.EMOJI_MAP.get(category, self.EMOJI_MAP["happy"])
        import random
        return random.choice(emojis)

    def add_emoji(self, text: str, category: str = "happy") -> str:
        """为文本添加表情"""
        return text + " " + self.random_emoji(category)


_tool: Optional[EmojiTool] = None


def get_emoji_tool() -> EmojiTool:
    global _tool
    if _tool is None:
        _tool = EmojiTool()
    return _tool