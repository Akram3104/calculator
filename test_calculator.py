from calculator import addition

# Custom test framework
class TestSuite:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def run_test(self, test_func):
        try:
            test_func()
            self.passed += 1
        except AssertionError as e:
            self.failed += 1
            print(f"Test failed: {e}")

    def summary(self):
        print(f"Tests passed: {self.passed}")
        print(f"Tests failed: {self.failed}")
        if self.failed > 0:
            exit(1)  # Exit with non-zero status code if any test fails

# Addition tests
def test_addition():
    assert addition(5, 3) == 8
    assert addition(-5, 3) == -2
    assert addition(0, 0) == 0

# Run tests
if __name__ == "__main__":
    suite = TestSuite()
    suite.run_test(test_addition)
    suite.summary()
