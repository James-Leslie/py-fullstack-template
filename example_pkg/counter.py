"""A simple counter module demonstrating Python package patterns."""


class Counter:
    """A counter that can be incremented and decremented.

    ## Example:

    ```python
    from example_pkg.counter import Counter


    counter = Counter(start=10)
    counter.increment()   # returns 11
    counter.decrement(5)  # returns 6
    counter.value         # 6
    ```
    """

    def __init__(self, start: int = 0) -> None:
        """
        Args:
            start: The initial value for the counter.
        """
        self._count = start

    @property
    def value(self) -> int:
        """Get the current count.

        Returns:
            The current counter value.
        """
        return self._count

    def increment(self, amount: int = 1) -> int:
        """Increment the counter and return the new value.

        Args:
            amount: The amount to increment by.

        Returns:
            The new counter value after incrementing.
        """
        self._count += amount
        return self._count

    def decrement(self, amount: int = 1) -> int:
        """Decrement the counter and return the new value.

        Args:
            amount: The amount to decrement by.

        Returns:
            The new counter value after decrementing.
        """
        self._count -= amount
        return self._count
