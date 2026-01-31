"""Tests for the Counter class."""

from example_pkg import Counter


def test_initial_value_default():
    """Counter starts at 0 by default."""
    counter = Counter()
    assert counter.value == 0


def test_initial_value_custom():
    """Counter can start at a custom value."""
    counter = Counter(start=10)
    assert counter.value == 10


def test_increment():
    """Increment increases the counter value."""
    counter = Counter()
    result = counter.increment()
    assert result == 1
    assert counter.value == 1

    result = counter.increment(5)
    assert result == 6
    assert counter.value == 6


def test_decrement():
    """Decrement decreases the counter value."""
    counter = Counter(start=10)
    result = counter.decrement()
    assert result == 9
    assert counter.value == 9

    result = counter.decrement(3)
    assert result == 6
    assert counter.value == 6
