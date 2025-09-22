import unittest

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers."""
    return a * b

def divide_numbers(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathOperations(unittest.TestCase):
    """Test cases for basic math operations."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        result = add_numbers(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero(self):
        """Test adding zero."""
        result = add_numbers(5, 0)
        self.assertEqual(result, 5)

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        result = multiply_numbers(4, 5)
        self.assertEqual(result, 20)

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        result = multiply_numbers(10, 0)
        self.assertEqual(result, 0)

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero_raises_error(self):
        """Test that dividing by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == '__main__':
    unittest.main()