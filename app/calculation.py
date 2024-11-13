from decimal import Decimal
from typing import Callable


class Calculation:
    """
    A class that represents a single mathematical calculation.

    Attributes:
        num1 (Decimal): The first value in the calculation.
        num2 (Decimal): The second value in the calculation.
        result (Decimal): The result of the operation.
        operation (Callable[[Decimal, Decimal], Decimal]): The mathematical function to execute.

    Methods:
        operate() -> Decimal:
            Executes the chosen operation on the operands and returns the outcome.

        create(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
            Static method that initializes a new Calculation instance.

        __repr__() -> str:
            Provides a string representation of the Calculation instance for easy readability.
    """

    def __init__(self, num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """
        Set up a Calculation instance with two values and a specified operation.

        Args:
            num1 (Decimal): The first number.
            num2 (Decimal): The second number.
            operation (Callable[[Decimal, Decimal], Decimal]): The arithmetic function to apply.
        """
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        self.result = self.operate()  # Automatically calculate the result upon instantiation

    def operate(self) -> Decimal:
        """
        Execute the assigned arithmetic function on the two values.

        Returns:
            Decimal: The result produced by the operation.
        """
        return self.operation(self.num1, self.num2)

    @staticmethod
    def create(num1: Decimal, num2: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """
        Initialize a new Calculation object.

        Args:
            num1 (Decimal): The first number.
            num2 (Decimal): The second number.
            operation (Callable[[Decimal, Decimal], Decimal]): The arithmetic function to apply.

        Returns:
            Calculation: A newly created Calculation instance.
        """
        return Calculation(num1, num2, operation)

    def __strrepr__(self) -> str:
        """
        Return a detailed string representation of this Calculation instance.

        Returns:
            str: A descriptive string of the Calculation instance.
        """
        return f"Calculation({self.num1}, {self.num2}, {self.operation.__name__}, {self.result})"
