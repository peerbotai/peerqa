#!/usr/bin/env python3
"""
Example test file for peerqa project.
This demonstrates basic testing functionality.
"""

def add_numbers(a, b):
    """Simple function to add two numbers."""
    return a + b

def multiply_numbers(a, b):
    """Simple function to multiply two numbers."""
    return a * b

def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("✓ add_numbers tests passed")

def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0
    print("✓ multiply_numbers tests passed")

def run_all_tests():
    """Run all tests."""
    print("Running tests...")
    test_add_numbers()
    test_multiply_numbers()
    print("All tests passed! ✅")

if __name__ == "__main__":
    run_all_tests()