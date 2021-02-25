import unittest
import pytest

from fibonacci import *


class FibonacciTester(unittest.TestCase):
    def testFibonacci(self):
        # Beginning can vary based on who is defining the fibonacci sequence
        # So we fully define the correct first three outputs
        
        self.assertEqual(0, fibonacci(0))
        self.assertEqual(1, fibonacci(1))
        self.assertEqual(1, fibonacci(2))

        # Testing higher fibonacci values

        self.assertEqual(34, fibonacci(9))
        self.assertEqual(144, fibonacci(12))
        self.assertEqual(377, fibonacci(14))

        # Negative inputs are undefined, at least in this program.
        self.assertRaises(ValueError, fibonacci, -14)

class FactorialTester(unittest.TestCase):
    def testFactorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))

        self.assertEqual(720, factorial(6))

        self.assertRaises(ValueError, factorial, -776)

class TestFibonacci:
    def test_zero(self):
        assert fibonacci(0) == 0
    def test_one(self):
        assert fibonacci(1) == 1
    def test_two(self):
        assert fibonacci(2) == 1

    def test_nine(self):
        assert fibonacci(9) == 34
    def test_twelve(self):
        assert fibonacci(12) == 144
    def test_fourteen(self):
        assert fibonacci(14) == 377

    def test_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-14)


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1
    def test_one(self):
        assert factorial(1) == 1
    def test_two(self):
        assert factorial(2) == 2

    def test_six(self):
        assert factorial(6) == 720

    def test_negative(self):
        with pytest.raises(ValueError):
            factorial(-776)


if __name__ == "__main__":
    unittest.main()
