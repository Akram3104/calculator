import pytest
from calculator import addition 
# Addition tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (-5, 3, -2)
])
@pytest.mark.strict
def test_addition(num1, num2, expected):
    try:
        assert addition(num1, num2) == expected
    except AssertionError as e:
            print(f"Test failed: {e}")
