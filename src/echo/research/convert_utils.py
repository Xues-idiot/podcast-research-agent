"""转换工具集合"""
from typing import Any, List


def str_to_int(s: str, default: int = 0) -> int:
    try:
        return int(s)
    except:
        return default


def str_to_float(s: str, default: float = 0.0) -> float:
    try:
        return float(s)
    except:
        return default


def str_to_bool(s: str) -> bool:
    return s.lower() in ('true', '1', 'yes', 'on')


def int_to_str(n: int) -> str:
    return str(n)


def float_to_str(n: float, decimals: int = 2) -> str:
    return f"{n:.{decimals}f}"


def bool_to_str(b: bool) -> str:
    return "true" if b else "false"


def list_to_str(lst: List, separator: str = ",") -> str:
    return separator.join(str(x) for x in lst)


def str_to_list(s: str, separator: str = ",", type_fn: Any = None) -> List:
    items = [x.strip() for x in s.split(separator)]
    if type_fn:
        return [type_fn(x) for x in items]
    return items


def dict_to_json(d: dict) -> str:
    import json
    return json.dumps(d)


def json_to_dict(s: str) -> dict:
    import json
    return json.loads(s)


def csv_to_list(s: str) -> List[List[str]]:
    import csv
    from io import StringIO
    reader = csv.reader(StringIO(s))
    return list(reader)


def list_to_csv(lst: List[List]) -> str:
    import csv
    from io import StringIO
    output = StringIO()
    writer = csv.writer(output)
    writer.writerows(lst)
    return output.getvalue()
