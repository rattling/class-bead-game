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


# now we only care about complete sets, kinda of a bingo situation when you build one up...can throw it into a list I guess.


def find_in_list_old(sublist, target):
    """
    Find the indices of the elements of `sublist` in `target`.

    If any element of `sublist` is not in `target`, return an empty list.
    The elements of `sublist` may not be unique and can appear in any order in `target`.

    Parameters:
        sublist (list): The list of elements to find in `target`.
        target (list): The list of elements to search in.

    Returns:
        list of lists: A list of occurrences of the sublist as a list of indices for each occurrence ordered by
        the elements of the sublist within each occurrence and the occurrences ordered by the first index of the occurrence


    Examples:
        find_in_list([2, 3, 2], [1, 2, 3, 2, 4]) -> [1, 2, 3]  # Found in sequence
        find_in_list([2, 3, 2], [3, 2, 6, 2, 4]) -> [1, 0, 3]  # Found in any order
        find_in_list([2, 3, 2], [1, 2, 3, 4]) -> []            # Second 2 not found
        find_in_list([1], [3, 1, 1, 5]) == [[1],[2]]  # Found single element sublist multiple times
        find_in_list([2, 3, 2], [1, 2, 3, 2, 4, 2, 3, 2]) == [
        [1, 2, 3],
        [5, 6, 7],]  # Found multi element sublist multiple times

    NB: This is nice and concise but performance will be quadratic time!
    """
    occurrences = []
    indices = []
    used_indices = set()
    # while len(used_indices) != len(target):
    while True:
        indices = []
        for v in sublist:
            for j, t in enumerate(target):
                if v == t and j not in used_indices:
                    indices.append(j)
                    used_indices.add(j)
                    break
            else:  # no break means no match found on this round. we are finished
                return occurrences
        occurrences.append(indices)


from typing import List


from typing import List


def find_in_list(
    sublist: List[int], target: List[int], ordered: bool = False
) -> List[List[int]]:
    """
    Find all occurrences of the `sublist` in the `target` in O(n) time where n is target list size.

    This function returns a list of occurrences where each occurrence is represented
    by a list of indices corresponding to the elements of the `sublist` in `target`.

    Parameters:
        sublist (List[int]): The list of elements to find in `target`.
        target (List[int]): The list of elements to search in.

    Returns:
        List[List[int]]: A list of lists, where each sublist represents the indices of
        one occurrence of the `sublist` in `target`. Returns an empty list if any
        element of `sublist` is not found in `target` or if no occurrences exist.

    Examples:
        >>> find_in_list([2, 3, 2], [1, 2, 3, 2, 4])
        [[1, 2, 3]]

        >>> find_in_list([2, 3, 2], [3, 2, 6, 2, 4])
        []

        >>> find_in_list([1], [3, 1, 1, 5])
        [[1], [2]]

        >>> find_in_list([2, 3, 2], [1, 2, 3, 2, 4, 2, 3, 2])
        [[1, 2, 3], [5, 6, 7]]
    """
    # Create a dictionary to map sublist elements to their indices in the target
    index_map = {element: [] for element in set(sublist)}

    # Populate the index_map with indices of matching elements in the target
    for index, value in enumerate(target):
        if value in index_map:
            index_map[value].append(index)

    # Check if any element in the sublist has no matches in the target
    if any(not indices for indices in index_map.values()):
        return []

    occurrences = []
    while True:
        current_occurrence = []
        for element in sublist:
            if index_map[element]:
                current_occurrence.append(index_map[element].pop(0))
            else:
                return occurrences
        occurrences.append(current_occurrence)


# lets add some basic tests for the functions and just leave them here for now.
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    winners = find_winners(items, lambda x: x)
    assert winners == [5, 5, 5, 5, 5, 5]

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

    assert find_in_list([2, 3, 2], [1, 2, 3, 2, 4]) == [[1, 2, 3]]  # Found in sequence
    assert find_in_list([2, 3, 2], [3, 2, 6, 2, 4]) == [[1, 0, 3]]  # Found in any order
    assert (
        find_in_list([2, 3, 2], [1, 2, 3, 4]) == []
    )  # Second 2 not found therefore pattern not found
    assert find_in_list([1], [3, 1, 1, 5]) == [
        [1],
        [2],
    ]  # Found single element sublist multiple times
    assert find_in_list([2, 3, 2], [1, 2, 3, 2, 4, 2, 3, 2]) == [
        [1, 2, 3],
        [5, 6, 7],
    ]  # Found in sequence

    assert find_in_list([7, 9, 5], [1, 2, 3, 4]) == []
