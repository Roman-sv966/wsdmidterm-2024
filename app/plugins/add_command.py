"""
This module defines the AddCommand class, which represents the addition operation.
It inherits from the Command base class and implements the execute method for performing the addition.
"""

from decimal import Decimal
from app.command import Command
from app.command_registry import register_command


class AddCommand(Command):
    """
    Command for performing addition of two decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the sum of two numbers.

    Attributes:
        a (Decimal): The first number to be added.
        b (Decimal): The second number to be added.
    """

    def __init__(self, a: Decimal, b: Decimal):
        """
        Initializes the AddCommand with two decimal numbers.

        Args:
            a (Decimal): The first number to be added.
            b (Decimal): The second number to be added.
        """
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """
        Executes the addition of two decimal numbers.

        Returns:
            Decimal: The sum of a and b.
        """
        return self.a + self.b


# Register the AddCommand in the global command registry with the name 'add'
register_command("add", AddCommand)
