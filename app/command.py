"""
Command module

This module defines the command classes that perform basic arithmetic operations 
such as addition, subtraction, multiplication, and division using Decimal values.
Each operation is implemented as a command that can be executed to obtain a result.
"""

from abc import ABC, abstractmethod
from decimal import Decimal
from app.command_registry import register_command
from queue import Queue


class Command(ABC):
    """
    Abstract base class for all commands.

    Each command must implement the execute method, which performs the 
    required calculation and returns a Decimal result.
    """

    @abstractmethod
    def execute(self) -> Decimal:
        """
        Executes the command and returns a result.

        Returns:
            Decimal: The result of the command's execution.

        Raises:
            NotImplementedError: If the method is not implemented.
        """
        raise NotImplementedError("Each command must implement the execute method.")

    def execute_in_process(self, result_queue: Queue) -> None:
        """
        Executes the command and places the result in the result queue.

        Args:
            result_queue (Queue): The queue to place the result or error.
        """
        try:
            result = self.execute()
            result_queue.put(result)
        except (ValueError, ZeroDivisionError) as e:
            result_queue.put(e)


class AddCommand(Command):
    """
    Command to perform addition of two Decimal values.
    """

    def __init__(self, operand1: Decimal, operand2: Decimal) -> None:
        """
        Initializes the AddCommand with two Decimal operands.

        Args:
            operand1 (Decimal): The first operand.
            operand2 (Decimal): The second operand.
        """
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self) -> Decimal:
        """
        Executes the addition operation.

        Returns:
            Decimal: The sum of operand1 and operand2.
        """
        return self.operand1 + self.operand2

register_command("add", AddCommand)


class SubtractCommand(Command):
    """
    Command to perform subtraction of two Decimal values.
    """

    def __init__(self, operand1: Decimal, operand2: Decimal) -> None:
        """
        Initializes the SubtractCommand with two Decimal operands.

        Args:
            operand1 (Decimal): The first operand.
            operand2 (Decimal): The second operand.
        """
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self) -> Decimal:
        """
        Executes the subtraction operation.

        Returns:
            Decimal: The result of subtracting operand2 from operand1.
        """
        return self.operand1 - self.operand2

register_command("subtract", SubtractCommand)


class MultiplyCommand(Command):
    """
    Command to perform multiplication of two Decimal values.
    """

    def __init__(self, operand1: Decimal, operand2: Decimal) -> None:
        """
        Initializes the MultiplyCommand with two Decimal operands.

        Args:
            operand1 (Decimal): The first operand.
            operand2 (Decimal): The second operand.
        """
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self) -> Decimal:
        """
        Executes the multiplication operation.

        Returns:
            Decimal: The product of operand1 and operand2.
        """
        return self.operand1 * self.operand2

register_command("multiply", MultiplyCommand)


class DivideCommand(Command):
    """
    Command to perform division of two Decimal values.
    """

    def __init__(self, operand1: Decimal, operand2: Decimal) -> None:
        """
        Initializes the DivideCommand with two Decimal operands.

        Args:
            operand1 (Decimal): The first operand.
            operand2 (Decimal): The second operand.
        """
        self.operand1 = operand1
        self.operand2 = operand2

    def execute(self) -> Decimal:
        """
        Executes the division operation.

        Returns:
            Decimal: The result of dividing operand1 by operand2.

        Raises:
            ValueError: If division by zero is attempted.
        """
        if self.operand2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.operand1 / self.operand2

register_command("divide", DivideCommand)
