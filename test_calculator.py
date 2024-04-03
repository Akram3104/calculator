import unittest
from calculator import addition, subtraction, multiplication, division, logarithm, square_root

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(5, 3), 8)
        self.assertEqual(addition(-5, 3), -2)
        self.assertEqual(addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)
        self.assertEqual(subtraction(5, -3), 8)
        self.assertEqual(subtraction(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
