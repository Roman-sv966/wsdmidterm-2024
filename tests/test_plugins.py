import pytest
import statistics
from decimal import Decimal
from app.plugins.add_command import AddCommand
from app.plugins.divide_command import DivideCommand
from app.plugins.mean_command import MeanCommand
from app.plugins.multiply_command import MultiplyCommand
from app.plugins.subtract_command import SubtractCommand
from app.plugins.mean_command import MeanCommand
from app.plugins.standard_deviation_command import StdDevCommand
from app.plugins.mode_command import ModeCommand

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

# Test MeanCommand
def test_mean_single_value():
    command = MeanCommand(Decimal('10.0'))
    result = command.execute()
    assert result == Decimal('10.0')

def test_mean_multiple_values():
    command = MeanCommand(Decimal('10.0'), Decimal('20.0'), Decimal('30.0'))
    result = command.execute()
    assert result == Decimal('20.0')

def test_mean_negative_values():
    command = MeanCommand(Decimal('-10.0'), Decimal('20.0'), Decimal('30.0'))
    result = command.execute()
    assert result == Decimal('13.33333333333333333333333333')  # Exact precision

def test_mean_empty():
    with pytest.raises(ValueError, match="At least one number must be provided."):
        MeanCommand().execute()

# Test StdDevCommand
def test_stddev_single_value():
    with pytest.raises(ValueError, match="At least two numbers must be provided to calculate standard deviation."):
        StdDevCommand(Decimal('10.0')).execute()

def test_stddev_two_values():
    command = StdDevCommand(Decimal('10.0'), Decimal('20.0'))
    result = command.execute()
    assert result == Decimal('7.0710678118654755')

def test_stddev_multiple_values():
    command = StdDevCommand(Decimal('10.0'), Decimal('20.0'), Decimal('30.0'), Decimal('40.0'))
    result = command.execute()
    assert result == Decimal('12.909944487358056') 

def test_stddev_negative_values():
    command = StdDevCommand(Decimal('-10.0'), Decimal('-20.0'), Decimal('-30.0'))
    result = command.execute()
    assert result == Decimal('10.0')

def test_stddev_identical_values():
    command = StdDevCommand(Decimal('10.0'), Decimal('10.0'), Decimal('10.0'))
    result = command.execute()
    assert result == Decimal('0.0')

# Test ModeCommand
def test_mode_single_value():
    command = ModeCommand(Decimal('5.0'))
    result = command.execute()
    assert result == Decimal('5.0')

def test_mode_multiple_values():
    command = ModeCommand(Decimal('5.0'), Decimal('3.0'), Decimal('5.0'))
    result = command.execute()
    assert result == Decimal('5.0')

def test_mode_negative_values():
    command = ModeCommand(Decimal('-5.0'), Decimal('-5.0'), Decimal('3.0'))
    result = command.execute()
    assert result == Decimal('-5.0')

