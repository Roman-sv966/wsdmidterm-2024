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
    Command for calculating the arithmetic mean (average) of multiple decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of calculating the mean of the provided numbers.

    Attributes:
        numbers (list of Decimal): The list of numbers for which the mean is calculated.
    """

    def __init__(self, *numbers: Decimal):
        """
        Initializes the MeanCommand with multiple decimal numbers.

        Args:
            numbers (Decimal): One or more decimal numbers for which the mean is calculated.
        """
        self.numbers = numbers

    def execute(self) -> Decimal:
        """
        Executes the calculation of the arithmetic mean of the provided decimal numbers.

        The mean is calculated by summing all numbers and dividing the result by the count of numbers.

        Returns:
            Decimal: The mean of the provided numbers.
        """
        if not self.numbers:
            raise ValueError("At least one number must be provided.")
        total = sum(self.numbers)
        return total / len(self.numbers)


# Register the MeanCommand in the global command registry with the name 'mean'
register_command("mean", MeanCommand)

