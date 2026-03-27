"""文本转表格工具"""

from typing import Optional


class TableFormatter:
    """文本转表格工具"""

    def to_csv_table(self, headers: list[str], rows: list[list[str]]) -> str:
        """转为CSV格式"""
        lines = [','.join(headers)]
        for row in rows:
            lines.append(','.join(row))
        return '\n'.join(lines)

    def to_markdown_table(self, headers: list[str], rows: list[list[str]]) -> str:
        """转为Markdown表格"""
        lines = []
        lines.append('| ' + ' | '.join(headers) + ' |')
        lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
        for row in rows:
            lines.append('| ' + ' | '.join(row) + ' |')
        return '\n'.join(lines)

    def to_tsv_table(self, headers: list[str], rows: list[list[str]]) -> str:
        """转为TSV格式"""
        lines = ['\t'.join(headers)]
        for row in rows:
            lines.append('\t'.join(row))
        return '\n'.join(lines)


_formatter: Optional[TableFormatter] = None


def get_table_formatter() -> TableFormatter:
    global _formatter
    if _formatter is None:
        _formatter = TableFormatter()
    return _formatter