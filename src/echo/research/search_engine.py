"""全文搜索工具"""

import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class SearchResult:
    """搜索结果"""
    line: str
    line_number: int
    match_start: int
    match_end: int


class FullTextSearch:
    """全文搜索引擎"""

    def search(self, text: str, query: str, case_sensitive: bool = False) -> list[SearchResult]:
        """搜索文本"""
        if not text or not query:
            return []

        results = []
        lines = text.split("\n")

        search_query = query if case_sensitive else query.lower()

        for line_num, line in enumerate(lines, 1):
            search_line = line if case_sensitive else line.lower()
            start = 0
            while True:
                pos = search_line.find(search_query, start)
                if pos == -1:
                    break
                results.append(SearchResult(
                    line=line,
                    line_number=line_num,
                    match_start=pos,
                    match_end=pos + len(query)
                ))
                start = pos + 1

        return results

    def search_regex(self, text: str, pattern: str) -> list[SearchResult]:
        """正则搜索"""
        if not text or not pattern:
            return []

        results = []
        lines = text.split("\n")
        compiled = re.compile(pattern)

        for line_num, line in enumerate(lines, 1):
            for match in compiled.finditer(line):
                results.append(SearchResult(
                    line=line,
                    line_number=line_num,
                    match_start=match.start(),
                    match_end=match.end()
                ))

        return results

    def count_matches(self, text: str, query: str) -> int:
        """计算匹配次数"""
        return len(self.search(text, query))


_searcher: Optional[FullTextSearch] = None


def get_full_text_search() -> FullTextSearch:
    global _searcher
    if _searcher is None:
        _searcher = FullTextSearch()
    return _searcher