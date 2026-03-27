"""列表zip工具"""

from typing import Optional, Any


class ListZip:
    """列表zip工具"""

    def zip_longest(self, *lists, fillvalue=None) -> list:
        """zip填充"""
        max_len = max(len(l) for l in lists)
        result = []
        for i in range(max_len):
            result.append(tuple(l[i] if i < len(l) else fillvalue for l in lists))
        return result

    def unzip(self, pairs: list) -> tuple:
        """解zip"""
        return tuple(list(x) for x in zip(*pairs))


_zip: Optional[ListZip] = None


def get_list_zip() -> ListZip:
    global _zip
    if _zip is None:
        _zip = ListZip()
    return _zip