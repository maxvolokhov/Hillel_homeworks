___doc___ = """Implement your own implementation of function max and min (* additional argument amount of result, 
if you pass 2, function should return 2 max values from the list)"""

from typing import List, Any

def max_analogue(iterable: List[Any], amount: int = 1) -> Any:
    max_values = []
    for _ in range(amount):
        current_max = iterable[0]
        for item in iterable:
            if item > current_max and item not in max_values:
                current_max = item
        max_values.append(current_max)
    return max_values

def min_analogue(iterable: List[Any], amount: int = 1) -> Any:
    min_values = []
    for _ in range(amount):
        current_min = iterable[0]
        for item in iterable:
            if item < current_min and item not in min_values:
                current_min = item
        min_values.append(current_min)
    return min_values
