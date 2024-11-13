"""
This module defines the DivideCommand class, which represents the division operation.
It inherits from the Command base class and implements the execute method for performing division.
"""

from decimal import Decimal
from app.command import Command
from app.command_registry import register_command


class DivideCommand(Command):
    """
    Command for performing division of two decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of dividing the first number by the second. If division by zero 
    is attempted, a ValueError is raised.

    Attributes:
        a (Decimal): The dividend, the number to be divided.
        b (Decimal): The divisor, the number by which to divide.
    """

    def __init__(self, a: Decimal, b: Decimal):
        """
        Initializes the DivideCommand with two decimal numbers.

        Args:
            a (Decimal): The number to be divided (dividend).
            b (Decimal): The number by which to divide (divisor).
        """
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """
        Executes the division of two decimal numbers.

        This method divides the first number by the second and returns the result. 
        If division by zero is attempted, a ValueError is raised.

        Returns:
            Decimal: The result of the division (a / b).

        Raises:
            ValueError: If b is zero, to prevent division by zero.
        """
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b


# Register the DivideCommand in the global command registry with the name 'divide'
register_command("divide", DivideCommand)
