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


# lets add a basic test for the find_winners function to run as script
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    winners = find_winners(items, lambda x: x)
    assert winners == [5, 5, 5, 5, 5, 5]
    print(winners)

    # Lets do one with an object and its method
    class Test:
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    items = [
        Test(1),
        Test(2),
        Test(3),
        Test(4),
        Test(5),
        Test(5),
        Test(5),
        Test(5),
        Test(5),
        Test(5),
    ]
    winners = find_winners(items, lambda x: x.get_value())
    assert set(winners) == set(
        [items[-1], items[-2], items[-3], items[-4], items[-5], items[-6]]
    )
