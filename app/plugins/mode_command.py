from decimal import Decimal
from app.command import Command
from app.command_registry import register_command
import statistics

class ModeCommand(Command):
    """
    Command for calculating the mode of multiple decimal numbers.

    This class inherits from the Command base class and implements the execute method 
    to return the result of calculating the mode of the provided numbers.

    Attributes:
        numbers (list of Decimal): The list of numbers for which the mode is calculated.
    """

    def __init__(self, *numbers: Decimal):
        """
        Initializes the ModeCommand with multiple decimal numbers.

        Args:
            numbers (Decimal): One or more decimal numbers for which the mode is calculated.
        """
        self.numbers = numbers

    def execute(self) -> Decimal:
        """
        Executes the calculation of the mode of the provided decimal numbers.

        Mode is calculated using the statistics library's mode function.

        Returns:
            Decimal: The mode of the provided numbers.
        """
        if not self.numbers:
            raise ValueError("At least one number must be provided to calculate mode.")
        
        # Convert Decimal to float for compatibility with statistics.mode
        numbers_float = [float(num) for num in self.numbers]
        mode_value = statistics.mode(numbers_float)
        
        return Decimal(str(mode_value))  # Convert result back to Decimal for consistency

# Register the ModeCommand in the global command registry with the name 'mode'
register_command("mode", ModeCommand)
