"""
This module defines the MultiplyCommand class, which represents the multiplication
of two decimal numbers. It inherits from the Command base class and implements 
the execute method to return the product of two numbers.
"""

from decimal import Decimal
from app.command import Command
from app.command_registry import register_command


class MultiplyCommand(Command):
    """
    Command for multiplying two decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of multiplying two numbers (a * b).

    Attributes:
        a (Decimal): The first number to be multiplied.
        b (Decimal): The second number to be multiplied.
    """

    def __init__(self, a: Decimal, b: Decimal):
        """
        Initializes the MultiplyCommand with two decimal numbers.

        Args:
            a (Decimal): The first number to be multiplied.
            b (Decimal): The second number to be multiplied.
        """
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """
        Executes the multiplication of two decimal numbers.

        The multiplication is performed by multiplying the two numbers.

        Returns:
            Decimal: The product of the two numbers (a * b).
        """
        return self.a * self.b


# Register the MultiplyCommand in the global command registry with the name 'multiply'
register_command("multiply", MultiplyCommand)
