___doc___ = """Implement your own all function"""

from typing import Iterable


def my_all(iterable: Iterable) -> bool:
    for item in iterable:
        if not item:
            return False
    return True
