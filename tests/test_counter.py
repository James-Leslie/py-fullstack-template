"""Tests for the Counter class."""

import pytest

from example_pkg import Counter


def test_initial_value_default():
    """Counter starts at 0 by default."""
    counter = Counter()
    assert counter.value == 0


@pytest.mark.parametrize("start", [-10, 0, 5, 100])
def test_initial_value_custom(start: int):
    """Counter can start at any integer value."""
    counter = Counter(start=start)
    assert counter.value == start


@pytest.mark.parametrize(
    "start, amount, expected",
    [
        (0, 1, 1),
        (0, 5, 5),
        (10, 3, 13),
    ],
)
def test_increment(start: int, amount: int, expected: int):
    """Increment increases the counter by the given amount."""
    counter = Counter(start=start)
    result = counter.increment(amount)
    assert result == expected
    assert counter.value == expected


@pytest.mark.parametrize(
    "start, amount, expected",
    [
        (10, 1, 9),
        (10, 3, 7),
        (0, 5, -5),
    ],
)
def test_decrement(start: int, amount: int, expected: int):
    """Decrement decreases the counter by the given amount."""
    counter = Counter(start=start)
    result = counter.decrement(amount)
    assert result == expected
    assert counter.value == expected


@pytest.mark.parametrize("amount", [0, -1, -100])
def test_increment_invalid_amount(amount: int):
    """Increment raises ValueError for non-positive amounts."""
    counter = Counter()
    with pytest.raises(ValueError):
        counter.increment(amount)


@pytest.mark.parametrize("amount", [0, -1, -100])
def test_decrement_invalid_amount(amount: int):
    """Decrement raises ValueError for non-positive amounts."""
    counter = Counter()
    with pytest.raises(ValueError):
        counter.decrement(amount)
