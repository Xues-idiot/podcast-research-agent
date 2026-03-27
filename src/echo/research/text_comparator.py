"""文本比较工具"""

from typing import Optional


class TextComparator:
    """文本比较工具"""

    def similarity_ratio(self, text1: str, text2: str) -> float:
        """相似度比率"""
        if not text1 or not text2:
            return 0.0
        set1 = set(text1.lower())
        set2 = set(text2.lower())
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union > 0 else 0.0

    def levenshtein_distance(self, text1: str, text2: str) -> int:
        """编辑距离"""
        if not text1:
            return len(text2)
        if not text2:
            return len(text1)

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if text1[i-1] == text2[j-1] else 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)

        return dp[m][n]

    def longest_common_substring(self, text1: str, text2: str) -> str:
        """最长公共子串"""
        if not text1 or not text2:
            return ""

        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        end_pos = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        end_pos = i

        return text1[end_pos - max_len:end_pos]


_comparator: Optional[TextComparator] = None


def get_text_comparator() -> TextComparator:
    global _comparator
    if _comparator is None:
        _comparator = TextComparator()
    return _comparator