from app.calculation import Calculation
from app.pandas_facade import PandasFacade
from decimal import Decimal
import os
import pandas as pd


class Calculations:
    """
    A class to track and manage a history of calculations using Pandas for flexible data handling.

    Attributes:
        history (PandasFacade): A PandasFacade instance to store calculation history.

    Methods:
        add_calculation(calculation: Calculation):
            Adds a new calculation to the history.

        clear_calculations():
            Clears all calculation records from the history.

        get_latest() -> Calculation:
            Retrieves the most recent calculation from the history, or None if history is empty.

        get_all_calculations() -> pd.DataFrame:
            Returns a DataFrame with all calculation records in the history.

        filter_by_operation(operation: str) -> pd.DataFrame:
            Filters the calculation history by the specified operation.

        save_history(filepath: str = "data/calculations.csv"):
            Saves the history DataFrame to a specified CSV file (defaults to 'data/calculations.csv').

        load_history(filepath: str = "data/calculations.csv"):
            Loads calculation history from a specified CSV file (defaults to 'data/calculations.csv').

        delete_calculation(index: int):
            Deletes a specific calculation from the history based on its index.
    """

    history = PandasFacade()

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Add a Calculation instance to the history DataFrame.

        Args:
            calculation (Calculation): The Calculation instance to add to history.
        """
        record = {
            "operation": calculation.operation.__name__,
            "num1": calculation.num1,
            "num2": calculation.num2,
            "result": calculation.result
        }
        cls.history.add_record(record)

    @classmethod
    def clear_calculations(cls):
        """
        Clear all calculation records from the history.
        """
        cls.history.clear_data()

    @classmethod
    def get_latest(cls) -> Calculation:
        """
        Get the most recent calculation entry from the history.

        Returns:
            Calculation: The latest Calculation in history, or None if no calculations exist.
        """
        if not cls.history.dataframe.empty:
            latest_record = cls.history.dataframe.iloc[-1]
            return Calculation(
                operation=latest_record["operation"],
                num1=Decimal(latest_record["num1"]),
                num2=Decimal(latest_record["num2"]),
                result=Decimal(latest_record["result"])
            )
        return None

    @classmethod
    def get_all_calculations(cls) -> pd.DataFrame:
        """
        Retrieve the full calculation history.

        Returns:
            pd.DataFrame: DataFrame of all calculations in the history.
        """
        return cls.history.dataframe

    @classmethod
    def filter_by_operation(cls, operation: str) -> pd.DataFrame:
        """
        Retrieve calculations that match the specified operation.

        Args:
            operation (str): The operation type to filter by (e.g., 'add', 'subtract').

        Returns:
            pd.DataFrame: DataFrame of calculations matching the specified operation.
        """
        return cls.history.filter_operations(operation)

    @classmethod
    def save_history(cls, filepath: str = "data/calculations.csv"):
        """
        Save the history DataFrame to a CSV file.

        Args:
            filepath (str): Path where the history will be saved. Defaults to 'data/calculations.csv'.
        """
        # Ensure the 'data' directory exists
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        cls.history.save_to_csv(filepath)

    @classmethod
    def load_history(cls, filepath: str = "data/calculations.csv"):
        """
        Load calculation history from a CSV file.

        Args:
            filepath (str): Path from which to load the history. Defaults to 'data/calculations.csv'.
        """
        if os.path.exists(filepath):
            cls.history.load_from_csv(filepath)
        else:
            print(f"Warning: File {filepath} not found. No data loaded.")

    @classmethod
    def delete_calculation(cls, index: int):
        """
        Delete a calculation record by its index.

        Args:
            index (int): The index of the calculation to delete.
        """
        cls.history.remove_record(index)
