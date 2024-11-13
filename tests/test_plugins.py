import pytest
from decimal import Decimal
from app.plugins.add_command import AddCommand
from app.plugins.divide_command import DivideCommand
from app.plugins.mean_command import MeanCommand
from app.plugins.multiply_command import MultiplyCommand
from app.plugins.subtract_command import SubtractCommand

# Test AddCommand
def test_add():
    command = AddCommand(Decimal('5.5'), Decimal('4.5'))
    result = command.execute()
    assert result == Decimal('10.0')

def test_add_negative():
    command = AddCommand(Decimal('-5.5'), Decimal('4.5'))
    result = command.execute()
    assert result == Decimal('-1.0')

# Test DivideCommand
def test_divide():
    command = DivideCommand(Decimal('10.0'), Decimal('2.0'))
    result = command.execute()
    assert result == Decimal('5.0')

def test_divide_by_zero():
    command = DivideCommand(Decimal('10.0'), Decimal('0.0'))
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()

def test_divide_negative():
    command = DivideCommand(Decimal('-10.0'), Decimal('2.0'))
    result = command.execute()
    assert result == Decimal('-5.0')

# Test MeanCommand
def test_mean():
    command = MeanCommand(Decimal('10.0'), Decimal('20.0'))
    result = command.execute()
    assert result == Decimal('15.0')

def test_mean_negative():
    command = MeanCommand(Decimal('-10.0'), Decimal('20.0'))
    result = command.execute()
    assert result == Decimal('5.0')

# Test MultiplyCommand
def test_multiply():
    command = MultiplyCommand(Decimal('5.0'), Decimal('4.0'))
    result = command.execute()
    assert result == Decimal('20.0')

def test_multiply_negative():
    command = MultiplyCommand(Decimal('-5.0'), Decimal('4.0'))
    result = command.execute()
    assert result == Decimal('-20.0')

# Test SubtractCommand
def test_subtract():
    command = SubtractCommand(Decimal('10.0'), Decimal('4.0'))
    result = command.execute()
    assert result == Decimal('6.0')

def test_subtract_negative():
    command = SubtractCommand(Decimal('-10.0'), Decimal('4.0'))
    result = command.execute()
    assert result == Decimal('-14.0')
