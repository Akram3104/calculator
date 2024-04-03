import pytest
import calculator

# Addition tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (-5, 3, -2),
    (0, 0, 0)
])
def test_addition(num1, num2, expected):
    assert calculator.add(num1, num2) == expected

# Subtraction tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (5, -3, 8),
    (0, 0, 0)
])
def test_subtraction(num1, num2, expected):
    assert calculator.subtract(num1, num2) == expected

# Multiplication tests
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 15),
    (-5, 3, -15),
    (0, 5, 0)
])
def test_multiplication(num1, num2, expected):
    assert calculator.multiply(num1, num2) == expected

# Division tests
@pytest.mark.parametrize("num1, num2, expected", [
    (10, 2, 5),
    (5, 0, "Error: Cannot divide by zero!")
])
def test_division(num1, num2, expected):
    if isinstance(expected, float):
        assert calculator.divide(num1, num2) == expected
    else:
        with pytest.raises(ZeroDivisionError):
            calculator.divide(num1, num2)

# Logarithmic tests
@pytest.mark.parametrize("num, expected", [
    (1, 0.0),
    (10, 2.302),
    (-1, "Error: Logarithm is not defined for negative numbers!")
])
def test_logarithm(num, expected):
    if isinstance(expected, float):
        assert calculator.logarithm(num) == pytest.approx(expected)
    else:
        with pytest.raises(ValueError) as excinfo:
            calculator.logarithm(num)
        assert str(excinfo.value) == expected

# Square root tests
@pytest.mark.parametrize("num, expected", [
    (25, 5.0),
    (-1, "Error: Square root is not defined for negative numbers!")
])
def test_square_root(num, expected):
    if isinstance(expected, float):
        assert calculator.square_root(num) == pytest.approx(expected)
    else:
        with pytest.raises(ValueError) as excinfo:
            calculator.square_root(num)
        assert str(excinfo.value) == expected
