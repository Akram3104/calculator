import pytest
from calculator import addition 
# Addition tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (-5, 3, -2)
])
@pytest.mark.strict
def test_addition(num1, num2, expected):
    assert addition(num1, num2) == expected

