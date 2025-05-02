"""Unit test for the add function."""

import pytest  # noqa: F401


def add(a: int, b: int) -> int:
    """Add two integers and return the result.

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns:
    -------
    int
        The sum of the two integers.
    """
    return a + b


# ---- Tests ----

EXPECTED_SUM = 5


def test_add() -> None:
    """Test the add function with two integers."""
    assert add(2, 3) == EXPECTED_SUM
