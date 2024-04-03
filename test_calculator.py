import pytest
import calculator

# Addition tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (-5, 3, -2),
    (0, 0, 0)
])
@pytest.mark.strict
def test_addition(num1, num2, expected):
    assert calculator.add(num1, num2) == expected

