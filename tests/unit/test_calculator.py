"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, multiplication, division

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5

    def test_subtract_negative_numbers(self):
        """Test adding negative numbers"""
        assert subtract(-2, -3) == 1
        assert subtract(-10, 5) == -15

class TestMultiplyDiv:
    """Test multiplication and division operations"""
    
    def test_multiplication_positive_numbers(self):
        """Test multiplication function"""
        assert multiplication(3, 4) == 12
        assert multiplication(0, 5) == 0

    def test_division_positive_numbers(self):
        """Test division function"""
        assert division(10, 2) == 5

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

class TestPowerSqrt:
    """Test power and square root functions"""
    
    def test_power_function(self):
        """Test power function"""
        from src.calculator import power
        assert power(2, 3) == 8
        assert power(5, 0) == 1
    
    def test_sqrt_function(self):
        """Test square root function"""
        from src.calculator import sqrt
        assert sqrt(16) == 4
        assert sqrt(0) == 0
        with pytest.raises(ValueError, match="Cannot compute square root of negative number"):
            sqrt(-4)

# TODO: Students will add TestMultiplyDivide class