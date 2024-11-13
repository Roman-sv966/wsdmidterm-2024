"""
Operations Module

This module provides fundamental arithmetic functions, including addition, 
subtraction, multiplication, and division. Each function accepts two inputs 
and returns the resulting value. The division function will raise an error 
if division by zero is attempted.
"""

from typing import Union


def add(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    """
    Calculate the sum of two numbers.

    Args:
        first_number (Union[int, float]): The first number.
        second_number (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The total of first_number and second_number. The result is of the same type as the inputs.
    """
    return first_number + second_number


def subtract(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    """
    Calculate the difference between two numbers.

    Args:
        first_number (Union[int, float]): The number to be reduced.
        second_number (Union[int, float]): The amount to subtract from first_number.

    Returns:
        Union[int, float]: The difference obtained from first_number - second_number.
    """
    return first_number - second_number


def multiply(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    """
    Calculate the product of two numbers.

    Args:
        first_number (Union[int, float]): The first number.
        second_number (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The multiplication result of first_number and second_number.
    """
    return first_number * second_number


def divide(first_number: Union[int, float], second_number: Union[int, float]) -> Union[int, float]:
    """
    Perform division of one number by another.

    Args:
        first_number (Union[int, float]): The number to be divided (dividend).
        second_number (Union[int, float]): The number by which to divide (divisor).

    Returns:
        Union[int, float]: The quotient resulting from first_number / second_number.

    Raises:
        ValueError: If second_number is zero, to prevent division by zero.
    """
    if second_number != 0:
        return first_number / second_number
    raise ValueError("Error: Cannot divide by zero!")
