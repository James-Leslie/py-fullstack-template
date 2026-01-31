"""A simple counter module demonstrating Python package patterns."""


class Counter:
    """A counter that can be incremented and decremented."""

    def __init__(self, start: int = 0) -> None:
        """Initialize the counter with an optional starting value."""
        self._count = start

    @property
    def value(self) -> int:
        """Get the current count."""
        return self._count

    def increment(self, amount: int = 1) -> int:
        """Increment the counter and return the new value."""
        self._count += amount
        return self._count

    def decrement(self, amount: int = 1) -> int:
        """Decrement the counter and return the new value."""
        self._count -= amount
        return self._count
