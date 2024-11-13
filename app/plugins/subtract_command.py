"""
This module defines the SubtractCommand class, which represents the subtraction
of two decimal numbers. It inherits from the Command base class and implements 
the execute method to return the result of subtracting the second number from the first.
"""

from decimal import Decimal
from app.command import Command
from app.command_registry import register_command


class SubtractCommand(Command):
    """
    Command for subtracting one decimal number from another.

    This class inherits from the Command base class and implements the execute method 
    to return the result of subtracting the second number (b) from the first (a).

    Attributes:
        a (Decimal): The number to subtract from.
        b (Decimal): The number to subtract.
    """

    def __init__(self, a: Decimal, b: Decimal):
        """
        Initializes the SubtractCommand with two decimal numbers.

        Args:
            a (Decimal): The number to subtract from.
            b (Decimal): The number to subtract.
        """
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """
        Executes the subtraction of two decimal numbers.

        The subtraction is performed by subtracting the second number (b) from 
        the first number (a).

        Returns:
            Decimal: The result of subtracting b from a (a - b).
        """
        return self.a - self.b


# Register the SubtractCommand in the global command registry with the name 'subtract'
register_command("subtract", SubtractCommand)
