import unittest
from calculator import addition, subtraction,multiply,divide,logarithm,square_root

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)
        self.assertEqual(addition(-5, 3), -2)
        self.assertEqual(addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(5, -3), 8)
        self.assertEqual(subtraction(0, 0), 0)
    def test_multiplication(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(0, 5), 0)
    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "Error: Cannot divide by zero!")
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(1), 0.0)
        self.assertAlmostEqual(logarithm(10), 2.303)
        self.assertAlmostEqual(logarithm(-1), "Error: Logarithm is not defined for non-positive numbers!")
    def test_square_root(self):
        self.assertAlmostEqual(square_root(25), 5.0)
        with self.assertRaises(ValueError):
            square_root(-1)
        



if __name__ == "__main__":
    unittest.main()
