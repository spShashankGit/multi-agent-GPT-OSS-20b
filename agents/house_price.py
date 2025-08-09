import pandas as pd

class HousePrince:
    """
    An agent to query the Boston House Prices dataset.
    """
    def __init__(self, file_path="housing.csv"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        """Loads the housing data from the specified CSV file."""
        try:
            # The metadata shows the data is space-separated and has no header
            column_names = [
                "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD",
                "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
            ]
            return pd.read_csv(self.file_path, delim_whitespace=True, names=column_names)
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found. Please ensure it is in the correct directory.")
            return None

    def query_data(self, query_string):
        """
        Queries the loaded dataset using a string-based query.
        Example: "RM > 7 and MEDV > 30"
        """
        if self.data is not None:
            try:
                return self.data.query(query_string)
            except Exception as e:
                return f"An error occurred while querying the data: {e}"
        return "Data is not loaded. Please check the file path."

# Example usage:
# if __name__ == "__main__":
#     agent = HousePrince()
#     if agent.data is not None:
#         # Find houses with more than 7 rooms and a median value over $30,000
#         result = agent.query_data("RM > 7 and MEDV > 30")
#         print("Query Result:")
#         print(result)

#         # Find the average crime rate (CRIM) for properties near the Charles River (CHAS=1)
#         result_chas = agent.query_data("CHAS == 1")
#         if not isinstance(result_chas, str) and not result_chas.empty:
#             avg_crim = result_chas['CRIM'].mean()
#             print(f"\\nAverage crime rate for properties near the Charles River: {avg_crim:.4f}")
#         else:
#             print("\\nNo data found for properties near the Charles River.")