# app/plugins/subtract_command.py
from decimal import Decimal
from app.command import Command
from app.command_registry import register_command

class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b

    def execute(self) -> Decimal:
        return self.a - self.b

register_command("subtract", SubtractCommand)