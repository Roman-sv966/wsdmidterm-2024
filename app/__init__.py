from decimal import Decimal
from typing import Callable

from app.operations import add, subtract, divide, multiply
from app.calculation import Calculation
from app.calculations import Calculations


class Calculator:
    """
    A class for performing basic arithmetic operations.

    Methods:
        perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
            Executes the specified operation on two Decimal values and records the calculation.

        add(a: Decimal, b: Decimal) -> Decimal:
            Calculates the sum of two Decimal values.

        subtract(a: Decimal, b: Decimal) -> Decimal:
            Computes the difference between two Decimal values.

        multiply(a: Decimal, b: Decimal) -> Decimal:
            Determines the product of two Decimal values.

        divide(a: Decimal, b: Decimal) -> Decimal:
            Finds the quotient when one Decimal value is divided by another.
    """

    @staticmethod
    def perform(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """
        Perform the specified arithmetic operation and logs the result for future reference.

        Args:
            a (Decimal): The first number in the operation.
            b (Decimal): The second number in the operation.
            operation (Callable[[Decimal, Decimal], Decimal]): The function representing the arithmetic operation.

        Returns:
            Decimal: The result of the arithmetic operation.
        """
        # Create and log the calculation
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        # Run the operation and return the output
        return calculation.operate()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Calculate the sum of two Decimal numbers."""
        return Calculator.perform(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Calculate the difference between two Decimal numbers."""
        return Calculator.perform(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Calculate the product of two Decimal numbers."""
        return Calculator.perform(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide one Decimal number by another."""
        return Calculator.perform(a, b, divide)
