import pytest
from app.calculation import Calculation
from app.calculations import Calculations
from app.operations import add, subtract, multiply, divide
from decimal import Decimal
import os

@pytest.fixture
def sample_calculations():
    """
    Fixture to populate history with sample calculations for testing.
    """
    # Clear existing calculations and add sample data
    Calculations.clear_calculations()

    # Adding sample calculations
    Calculations.add_calculation(Calculation(Decimal('7'), Decimal('2'), add))
    Calculations.add_calculation(Calculation(Decimal('5'), Decimal('3'), subtract))
    Calculations.add_calculation(Calculation(Decimal('6'), Decimal('4'), multiply))
    Calculations.add_calculation(Calculation(Decimal('8'), Decimal('2'), divide))


def test_get_all_calculations(sample_calculations):
    """
    Test retrieving all calculations from history.
    """
    history = Calculations.get_all_calculations()
    assert len(history) == 4, "Incorrect number of entries in history."


def test_filter_by_operation(sample_calculations):
    """
    Test filtering calculations by operation type.
    """
    add_results = Calculations.filter_by_operation("add")
    assert len(add_results) == 1, "Incorrect count of 'add' operations."

    subtract_results = Calculations.filter_by_operation("subtract")
    assert len(subtract_results) == 1, "Incorrect count of 'subtract' operations."

    multiply_results = Calculations.filter_by_operation("multiply")
    assert len(multiply_results) == 1, "Incorrect count of 'multiply' operations."

    divide_results = Calculations.filter_by_operation("divide")
    assert len(divide_results) == 1, "Incorrect count of 'divide' operations."


def test_clear_calculations(sample_calculations):
    """
    Test clearing all calculations from history.
    """
    Calculations.clear_calculations()
    history = Calculations.get_all_calculations()
    assert len(history) == 0, "History was not cleared."



def test_delete_calculation(sample_calculations):
    """
    Test deleting a specific calculation from the history.
    """
    # Get the index of the first calculation
    index_to_delete = 0  # The index of the first added calculation

    # Delete the calculation at the specified index
    Calculations.delete_calculation(index_to_delete)

    # Check if the history size has reduced by 1
    history = Calculations.get_all_calculations()
    assert len(history) == 3, "Failed to delete calculation."


def test_delete_calculation_with_invalid_index(sample_calculations):
    """
    Test deleting a calculation with an invalid index.
    """
    invalid_index = 100  # Invalid index, larger than the number of records in history
    Calculations.delete_calculation(invalid_index)

    # Check if the history is unchanged
    history = Calculations.get_all_calculations()
    assert len(history) == 4, "History was modified with an invalid index."


def test_get_latest_after_clear():
    """
    Test retrieving the latest calculation after clearing the history.
    """
    Calculations.clear_calculations()
    latest = Calculations.get_latest()
    assert latest is None, "History is empty, but get_latest returned a value."


# Running the tests using pytest
if __name__ == "__main__":
    pytest.main()
