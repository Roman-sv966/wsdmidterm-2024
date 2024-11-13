"""
This module defines the PandasFacade class, which simplifies typical DataFrame operations,
such as adding and removing records, filtering by criteria, and saving/loading data to/from files.
"""

import pandas as pd
from typing import Dict


class PandasFacade:
    """
    Simplifies common data operations on a Pandas DataFrame.
    """

    def __init__(self):
        """
        Initializes the PandasFacade with a DataFrame containing default columns.

        The DataFrame will have columns: 'operation', 'num1', 'num2', 'result'.
        """
        self.dataframe: pd.DataFrame = pd.DataFrame(columns=["operation", "num1", "num2", "result"])

    def add_record(self, record: Dict[str, str]) -> None:
        """
        Appends a new entry to the DataFrame.

        Args:
            record (Dict[str, str]): Dictionary containing details of an operation. 
                Keys must match the DataFrame columns: 'operation', 'num1', 'num2', 'result'.
        """
        self.dataframe = pd.concat([self.dataframe, pd.DataFrame([record])], ignore_index=True)

    def clear_data(self) -> None:
        """
        Resets the DataFrame, removing all records and keeping the column headers.
        """
        self.dataframe = pd.DataFrame(columns=self.dataframe.columns)

    def filter_operations(self, operation: str) -> pd.DataFrame:
        """
        Filters records by operation type.

        Args:
            operation (str): The operation name to filter by.

        Returns:
            pd.DataFrame: DataFrame containing only the records matching the specified operation.
        """
        return self.dataframe[self.dataframe["operation"] == operation]

    def save_to_csv(self, filepath: str) -> None:
        """
        Exports the DataFrame to a CSV file.

        Args:
            filepath (str): The file path where the DataFrame should be saved.
        """
        self.dataframe.to_csv(filepath, index=False)

    def load_from_csv(self, filepath: str) -> None:
        """
        Imports data from a CSV file into the DataFrame.

        Args:
            filepath (str): Path to the CSV file to load.
        """
        self.dataframe = pd.read_csv(filepath)

    def remove_record(self, index: int) -> None:
        """
        Removes a record by its index position.

        Args:
            index (int): Index of the record to delete.
        
        Raises:
            IndexError: If the provided index is out of bounds of the DataFrame.
        """
        if 0 <= index < len(self.dataframe):
            self.dataframe = self.dataframe.drop(index).reset_index(drop=True)
            print(f"Record at index {index} removed.")
        else:
            print(f"Index {index} is out of bounds. Deletion unsuccessful.")
