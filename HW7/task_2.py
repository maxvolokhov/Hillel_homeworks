___doc___ = """Implement your realization of the function filter """

from typing import Callable, Any, List


def filter_analogue(function: Callable[[Any], bool], sequence: List[Any]) -> List[Any]:
    filtered_list = []
    for item in sequence:
        if function(item):
            filtered_list.append(item)
    return filtered_list
