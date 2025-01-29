import pytest

from casino.collection_utils import (
    find_winners,
    Comparison,
)


def test_find_winners_basic():
    items = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    winners = find_winners(items, lambda x: x)
    assert winners == [5, 5, 5, 5, 5, 5]


def test_find_winners_with_lambda():
    items = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
    winners = find_winners(items, lambda x: -x)
    assert winners == [1]


def test_find_winners_with_custom_objects():

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


def test_winners_with_dict_basic():
    items = {"Alice": 100, "Bob": 200, "Charlie": 300, "David": 400}
    winners = find_winners(items)
    assert winners == ["David"]


def test_winners_with_dict_lambda():
    items = {"Alice": 100, "Bob": 200, "Charlie": 300, "David": 400}
    winners = find_winners(items, lambda x: -x)
    assert winners == ["Alice"]


def test_winners_with_ist_of_dicts():
    products = [
        {"name": "A", "price": 10},
        {"name": "B", "price": 20},
        {"name": "C", "price": 10},
    ]
    cheapest = find_winners(
        products, key=lambda p: p["price"], comparison=Comparison.MIN
    )
    print([p["name"] for p in cheapest])  # ['A', 'C']
