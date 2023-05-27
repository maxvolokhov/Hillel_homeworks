___doc___ = """Implement your own implementation of the function map"""


from typing import Callable, Any, Iterable

def map_analogue(function: Callable[[Any], Any], iterable: Iterable) -> Iterable:
    mapped_list = []
    for item in iterable:
        mapped_list.append(function(item))
    return mapped_list
