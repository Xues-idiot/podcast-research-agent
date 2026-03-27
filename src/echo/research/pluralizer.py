"""复数形式工具"""

from typing import Optional


class Pluralizer:
    """复数形式工具"""

    IRREGULAR = {
        "person": "people",
        "man": "men",
        "woman": "women",
        "child": "children",
        "tooth": "teeth",
        "foot": "feet",
        "mouse": "mice",
        "ox": "oxen",
    }

    def pluralize(self, word: str) -> str:
        """复数形式"""
        if word.lower() in self.IRREGULAR:
            return self.IRREGULAR[word.lower()]
        if word.endswith('y') and len(word) > 1 and word[-2] not in 'aeiou':
            return word[:-1] + 'ies'
        if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return word + 'es'
        return word + 's'


_pluralizer: Optional[Pluralizer] = None


def get_pluralizer() -> Pluralizer:
    global _pluralizer
    if _pluralizer is None:
        _pluralizer = Pluralizer()
    return _pluralizer