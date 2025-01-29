from typing import TypeVar, Callable, Union, Sequence, Dict, List
from enum import Enum

T = TypeVar("T")  # Type of items in sequences
K = TypeVar("K")  # Type of keys in dictionaries
V = TypeVar("V")  # Type of values in dictionaries
U = TypeVar("U")  # Return type of the key function


class Comparison(Enum):
    MAX = "max"
    MIN = "min"


def find_winners(
    items: Union[Sequence[T], Dict[K, V]],
    key: Callable[[Union[T, V]], U] = None,
    comparison: Union[str, Comparison] = Comparison.MAX,
) -> List[Union[T, K]]:
    """
    Finds all items in `items` that meet the comparison criteria according to the `key` function.

    Args:
        items: A sequence (like a list or tuple) or a dictionary.
        key: A callable that determines the comparison value for each item.
             - For sequences, it takes an item of type T and returns a value of type U.
             - For dictionaries, it takes a value of type V and returns a value of type U.
             If not provided, defaults to:
                 - For sequences: the item itself (identity).
                 - For dictionaries: the dictionary's values.
        comparison: A string specifying the comparison method or a Comparison enum.
                    Allowed values: 'max', 'min', Comparison.MAX, Comparison.MIN.
                    Defaults to Comparison.MAX.

    Returns:
        A list of "winner" items:
            - If `items` is a sequence, returns a list of items with the maximum/minimum key value.
            - If `items` is a dictionary, returns a list of keys whose corresponding values have the maximum/minimum key value.

    Examples:
        # Find the maximum value(s) in a list
        items = [1, 2, 3, 4, 5, 5]
        winners = find_winners(items)
        print(winners)  # Output: [5, 5]

        # Find the minimum value(s) in a list
        items = [1, 2, 3, 4, 5]
        winners = find_winners(items, comparison=Comparison.MIN)
        print(winners)  # Output: [1]

        # Use a custom key function for complex objects
        class Test:
            def __init__(self, value):
                self.value = value

        items = [Test(1), Test(2), Test(3)]
        winners = find_winners(items, key=lambda x: x.value)
        print([w.value for w in winners])  # Output: [3]

        # Find the highest-scoring player in a dictionary
        scores = {"Alice": 90, "Bob": 95, "Charlie": 95, "David": 85}
        winners = find_winners(scores)
        print(winners)  # Output: ['Bob', 'Charlie']

        # Find the cheapest product in a list of dictionaries
        products = [{"name": "A", "price": 10}, {"name": "B", "price": 20}, {"name": "C", "price": 10}]
        cheapest = find_winners(products, key=lambda p: p["price"], comparison=Comparison.MIN)
        print([p["name"] for p in cheapest])  # Output: ['A', 'C']

    """
    if not items:
        return []

    # Convert string comparison to enum if necessary
    if isinstance(comparison, str):
        try:
            comparison = Comparison(comparison)
        except ValueError:
            raise ValueError(
                f"Invalid comparison '{comparison}'. Allowed values are {list(Comparison)}."
            )

    # Define the function for the desired comparison
    comparison_func = {"max": max, "min": min}[comparison.value]

    # Determine the key function and iterable based on item type
    if isinstance(items, dict):
        key_func = (lambda k: key(items[k])) if key else (lambda k: items[k])
        iterable = items.keys()
    elif isinstance(items, Sequence):
        key_func = key or (lambda x: x)  # Default to identity
        iterable = items
    else:
        raise TypeError("Items must be either a sequence or a dictionary.")

    # Find the target value using the comparison function
    try:
        target_value = comparison_func(key_func(item) for item in iterable)
    except Exception as e:
        raise ValueError(f"Error computing {comparison.value} value: {e}")

    # Collect all items that match the target value
    return [item for item in iterable if key_func(item) == target_value]
