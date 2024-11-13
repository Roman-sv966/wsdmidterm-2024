"""
This module defines the PandasFacade class, which simplifies typical DataFrame operations,
such as adding and removing records, filtering by criteria, and saving/loading data to/from files.
"""

import pandas as pd

class PandasFacade:
    """
    Simplifies common data operations on a Pandas DataFrame.
    """

    def __init__(self):
        # Initialize DataFrame with default columns
        self.dataframe = pd.DataFrame(columns=["operation", "num1", "num2", "result"])

    def add_record(self, record: dict):
        """
        Appends a new entry to the DataFrame.

        Args:
            record (dict): Dictionary containing details of an operation.
        """
        self.dataframe = pd.concat([self.dataframe, pd.DataFrame([record])], ignore_index=True)

    def clear_data(self):
        """
        Resets the DataFrame, removing all records.
        """
        self.dataframe = pd.DataFrame(columns=self.dataframe.columns)

    def filter_operations(self, operation: str) -> pd.DataFrame:
        """
        Filters records by operation type.

        Args:
            operation (str): Operation name to filter by.

        Returns:
            pd.DataFrame: DataFrame containing only the filtered records.
        """
        return self.dataframe[self.dataframe["operation"] == operation]

    def save_to_csv(self, filepath: str):
        """
        Exports the DataFrame to a CSV file.

        Args:
            filepath (str): File path where the DataFrame should be saved.
        """
        self.dataframe.to_csv(filepath, index=False)

    def load_from_csv(self, filepath: str):
        """
        Imports data from a CSV file into the DataFrame.

        Args:
            filepath (str): Path to the CSV file to load.
        """
        self.dataframe = pd.read_csv(filepath)

    def remove_record(self, index: int):
        """
        Removes a record by its index position.

        Args:
            index (int): Index of the record to delete.
        """
        if 0 <= index < len(self.dataframe):
            self.dataframe = self.dataframe.drop(index).reset_index(drop=True)
            print(f"Record at index {index} removed.")
        else:
            print(f"Index {index} is out of bounds. Deletion unsuccessful.")
