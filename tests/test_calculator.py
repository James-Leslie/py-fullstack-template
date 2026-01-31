"""Tests for the calculator module."""

import pytest

from example_pkg import (
    Calculator,
    DivisionByZeroError,
    add,
    divide,
    multiply,
    subtract,
)


class TestStandaloneFunctions:
    """Tests for standalone arithmetic functions."""

    def test_add_positive_numbers(self) -> None:
        assert add(2, 3) == 5

    def test_add_negative_numbers(self) -> None:
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self) -> None:
        assert add(-2, 3) == 1

    def test_add_floats(self) -> None:
        assert add(2.5, 3.5) == 6.0

    def test_subtract_positive_numbers(self) -> None:
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self) -> None:
        assert subtract(3, 5) == -2

    def test_multiply_positive_numbers(self) -> None:
        assert multiply(4, 3) == 12

    def test_multiply_by_zero(self) -> None:
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self) -> None:
        assert multiply(-2, -3) == 6

    def test_divide_positive_numbers(self) -> None:
        assert divide(10, 2) == 5

    def test_divide_with_remainder(self) -> None:
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self) -> None:
        with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
            divide(10, 0)


class TestCalculator:
    """Tests for the Calculator class."""

    def test_calculator_starts_with_empty_history(self) -> None:
        calc = Calculator()
        assert calc.history == []

    def test_last_result_is_none_when_empty(self) -> None:
        calc = Calculator()
        assert calc.last_result is None

    def test_add_records_history(self) -> None:
        calc = Calculator()
        result = calc.add(2, 3)
        assert result == 5
        assert calc.history == [("2 + 3", 5)]

    def test_subtract_records_history(self) -> None:
        calc = Calculator()
        result = calc.subtract(5, 3)
        assert result == 2
        assert calc.history == [("5 - 3", 2)]

    def test_multiply_records_history(self) -> None:
        calc = Calculator()
        result = calc.multiply(4, 3)
        assert result == 12
        assert calc.history == [("4 * 3", 12)]

    def test_divide_records_history(self) -> None:
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5
        assert calc.history == [("10 / 2", 5)]

    def test_divide_by_zero_raises_error(self) -> None:
        calc = Calculator()
        with pytest.raises(DivisionByZeroError):
            calc.divide(10, 0)

    def test_last_result_returns_most_recent(self) -> None:
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert calc.last_result == 12

    def test_clear_history(self) -> None:
        calc = Calculator()
        calc.add(1, 2)
        calc.multiply(3, 4)
        calc.clear_history()
        assert calc.history == []
        assert calc.last_result is None

    def test_multiple_operations_build_history(self) -> None:
        calc = Calculator()
        calc.add(1, 2)
        calc.subtract(5, 3)
        calc.multiply(2, 4)
        assert len(calc.history) == 3
        assert calc.history[0] == ("1 + 2", 3)
        assert calc.history[1] == ("5 - 3", 2)
        assert calc.history[2] == ("2 * 4", 8)
