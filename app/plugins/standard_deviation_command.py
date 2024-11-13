from decimal import Decimal
from app.command import Command
from app.command_registry import register_command
import statistics

class StdDevCommand(Command):
    """
    Command for calculating the standard deviation of multiple decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of calculating the standard deviation of the provided numbers.

    Attributes:
        numbers (list of Decimal): The list of numbers for which the standard deviation is calculated.
    """

    def __init__(self, *numbers: Decimal):
        """
        Initializes the StdDevCommand with multiple decimal numbers.

        Args:
            numbers (Decimal): One or more decimal numbers for which the standard deviation is calculated.
        """
        self.numbers = numbers

    def execute(self) -> Decimal:
        """
        Executes the calculation of the standard deviation of the provided decimal numbers.

        Standard deviation is calculated using the statistics library's stdev function.

        Returns:
            Decimal: The standard deviation of the provided numbers.
        """
        if len(self.numbers) < 2:
            raise ValueError("At least two numbers must be provided to calculate standard deviation.")
        
        # Convert Decimal to float for compatibility with statistics.stdev
        numbers_float = [float(num) for num in self.numbers]
        stddev_value = statistics.stdev(numbers_float)
        
        return Decimal(str(stddev_value))  # Convert result back to Decimal for consistency

# Register the StdDevCommand in the global command registry with the name 'stddev'
register_command("stddev", StdDevCommand)
