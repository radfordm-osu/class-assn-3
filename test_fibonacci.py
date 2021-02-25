import unittest
import fibonacci

class CalcTester(unittest.TestCase):
    def test_low(self):
        result = fibonacci.Fibonacci(4)
        self.assertEqual(result, 2)

    def test_high(self):
        result = fibonacci.Fibonacci(12)
        self.assertEqual(result, 89)

    def test_word(self):
        result = fibonacci.Fibonacci("Word")
        self.assertEqual(result, -1)

    def test_zero(self):
        result = fibonacci.Fibonacci(0)
        self.assertEqual(result, -1)

    def test_none(self):
        result = fibonacci.Fibonacci("")
        self.assertEqual(result, -1)

    def test_fact_word(self):
        result = fibonacci.Factorial("Word")
        self.assertEqual(result, -1)

    def test_fac_zero(self):
        result = fibonacci.Factorial(0)
        self.assertEqual(result, -1)

    def test_fact(self):
        result = fibonacci.Factorial(6)
        self.assertEqual(result, 720)

    if __name__ == "__main__":
        unittest.main()
