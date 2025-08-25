import pandas as pd

class AirlineFlights:
    """
    An agent to query the Airlines Flights dataset.
    """
    def __init__(self, file_path="airlines_flights_data.csv"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        """Loads the airline flights data from the specified CSV file."""
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found. Please ensure it is in the correct directory.")
            return None

    def query_data(self, query_string):
        """
        Queries the loaded dataset using a string-based query.
        Example: "airline == 'SpiceJet' and class == 'Economy'"
        """
        if self.data is not None:
            try:
                return self.data.query(query_string)
            except Exception as e:
                return f"An error occurred while querying the data: {e}"
        return "Data is not loaded. Please check the file path."

    def get_airline_summary(self):
        """Get a summary of airlines and their flight counts."""
        if self.data is not None:
            return self.data['airline'].value_counts()
        return "Data is not loaded."

    def get_price_statistics(self, airline=None):
        """Get price statistics, optionally filtered by airline."""
        if self.data is not None:
            if airline:
                filtered_data = self.data[self.data['airline'] == airline]
                if filtered_data.empty:
                    return f"No data found for airline: {airline}"
                return filtered_data['price'].describe()
            return self.data['price'].describe()
        return "Data is not loaded."

    def get_routes_summary(self):
        """Get a summary of popular routes."""
        if self.data is not None:
            routes = self.data['source_city'] + ' -> ' + self.data['destination_city']
            return routes.value_counts().head(10)
        return "Data is not loaded."

# Example usage:
# if __name__ == "__main__":
#     agent = AirlineFlights()
#     if agent.data is not None:
#         # Find all SpiceJet flights from Delhi to Mumbai
#         result = agent.query_data("airline == 'SpiceJet' and source_city == 'Delhi' and destination_city == 'Mumbai'")
#         print("SpiceJet Delhi to Mumbai flights:")
#         print(result)
#
#         # Get airline summary
#         print("\nAirline Summary:")
#         print(agent.get_airline_summary())
#
#         # Get price statistics for Vistara
#         print("\nVistara Price Statistics:")
#         print(agent.get_price_statistics('Vistara'))