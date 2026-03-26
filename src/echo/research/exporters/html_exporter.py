"""HTML格式化工具"""

from typing import Optional


class HTMLFormatter:
    """HTML格式化器"""

    @staticmethod
    def escape(text: str) -> str:
        return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))

    @staticmethod
    def format_header(text: str, level: int = 1) -> str:
        return f"<h{level}>{text}</h{level}>\n"

    @staticmethod
    def format_paragraph(text: str) -> str:
        return f"<p>{text}</p>\n"

    @staticmethod
    def format_bold(text: str) -> str:
        return f"<strong>{text}</strong>"

    @staticmethod
    def format_link(text: str, url: str) -> str:
        return f'<a href="{url}">{text}</a>'

    @staticmethod
    def format_list(items: list, ordered: bool = False) -> str:
        tag = "ol" if ordered else "ul"
        items_html = "".join(f"<li>{item}</li>" for item in items)
        return f"<{tag}>\n{items_html}\n</{tag}>\n"

    @staticmethod
    def format_card(title: str, content: str, color: str = "#3498DB") -> str:
        return f'''
<div class="card" style="border-left: 4px solid {color};">
    <h3>{title}</h3>
    <p>{content}</p>
</div>
'''

    @staticmethod
    def format_table(headers: list, rows: list) -> str:
        lines = ["<table>", "<thead>", "<tr>"]
        for h in headers:
            lines.append(f"<th>{h}</th>")
        lines.append("</tr></thead><tbody>")
        for row in rows:
            lines.append("<tr>")
            for cell in row:
                lines.append(f"<td>{cell}</td>")
            lines.append("</tr>")
        lines.append("</tbody></table>")
        return "\n".join(lines) + "\n"


_html_formatter: Optional[HTMLFormatter] = None

def get_html_formatter() -> HTMLFormatter:
    global _html_formatter
    if _html_formatter is None:
        _html_formatter = HTMLFormatter()
    return _html_formatter
