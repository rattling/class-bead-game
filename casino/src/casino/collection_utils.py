# collection_utils.py
from typing import List, Callable, TypeVar, Sequence

T = TypeVar("T")


def find_winners(items: Sequence[T], key: Callable[[T], float]) -> List[T]:
    """
    Generic function to find all items that have the maximum value according to the key function.
    """
    if not items:
        return []
    max_value = max(key(item) for item in items)
    return [item for item in items if key(item) == max_value]
