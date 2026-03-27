"""单词拆分工具"""

from typing import List, Optional


class WordBreak:
    _instance: Optional["WordBreak"] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def can_break(self, s: str, word_dict: List[str]) -> bool:
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


def get_word_break() -> WordBreak:
    return WordBreak()
