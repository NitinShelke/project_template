"""Unit test for the add function."""

import pytest  # noqa: F401

from project.core import add


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),  # integer addition
        (-2, -3, -5),  # negative numbers
        (0, 9, 9),  # zero with number
        (3.5, 3.5, 7.0),  # floats
        (5, 1.5, 6.5),  # int + float
    ],
)
def test_add_valid_inputs(a: int, b: int, expected: int) -> None:
    """Test the add function with valid inputs.

    Parameters
    ----------
    a : int or float
        The first operand.
    b : int or float
        The second operand.
    expected : int or float
        The expected result of the addition.
    """
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("1", 2),  # string input
        (None, 4),  # None input
        ([1, 2], 3),  # list input
        ({"x": 1}, 2),  # dict input
    ],
)
def test_add_invalid_inputs(a: int, b: int) -> None:
    """Test the add function with invalid inputs.

    Parameters
    ----------
    a : int or float
        The first operand.
    b : int or float
        The second operand.

    Raises:
    ------
    TypeError
        If the inputs are of invalid types.
    """
    with pytest.raises(TypeError):
        add(a, b)
