"""A simple calculator module demonstrating Python best practices.

This module provides basic arithmetic operations as both standalone functions
and through a Calculator class that maintains operation history.
"""

from dataclasses import dataclass, field


class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""


def add(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a divided by b.

    Raises:
        DivisionByZeroError: If b is zero.
    """
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b


@dataclass
class Calculator:
    """A calculator that tracks operation history.

    Attributes:
        history: A list of tuples containing (operation, result) pairs.
    """

    history: list[tuple[str, float]] = field(default_factory=list)

    @property
    def last_result(self) -> float | None:
        """Get the result of the last operation, or None if no operations performed."""
        if not self.history:
            return None
        return self.history[-1][1]

    def add(self, a: float, b: float) -> float:
        """Add two numbers and record in history."""
        result = add(a, b)
        self.history.append((f"{a} + {b}", result))
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers and record in history."""
        result = subtract(a, b)
        self.history.append((f"{a} - {b}", result))
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and record in history."""
        result = multiply(a, b)
        self.history.append((f"{a} * {b}", result))
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers and record in history."""
        result = divide(a, b)
        self.history.append((f"{a} / {b}", result))
        return result

    def clear_history(self) -> None:
        """Clear all operation history."""
        self.history.clear()
