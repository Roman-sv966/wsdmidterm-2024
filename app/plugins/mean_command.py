"""
This module defines the MeanCommand class, which represents the calculation 
of the arithmetic mean (average) of two decimal numbers.
It inherits from the Command base class and implements the execute method 
to return the mean of two numbers.
"""

from decimal import Decimal
from app.command import Command
from app.command_registry import register_command


class MeanCommand(Command):
    """
    Command for calculating the arithmetic mean (average) of two decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of calculating the mean of two numbers (a + b) / 2.

    Attributes:
        a (Decimal): The first number in the pair.
        b (Decimal): The second number in the pair.
    """

    def __init__(self, a: Decimal, b: Decimal):
        """
        Initializes the MeanCommand with two decimal numbers.

        Args:
            a (Decimal): The first number for which the mean is calculated.
            b (Decimal): The second number for which the mean is calculated.
        """
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        """
        Executes the calculation of the arithmetic mean of two decimal numbers.

        The mean is calculated by adding the two numbers and dividing the result by 2.

        Returns:
            Decimal: The mean of the two numbers (a + b) / 2.
        """
        return (self.a + self.b) / 2


# Register the MeanCommand in the global command registry with the name 'mean'
register_command("mean", MeanCommand)
