import os
from langchain.tools import tool
from agents.house_price import HousePrince
from agents.airline_flights import AirlineFlights

# Initialize the data agents with proper file paths
data_dir = "/home/runner/work/multi-agent-GPT-OSS-20b/multi-agent-GPT-OSS-20b/data"
house_data_path = os.path.join(data_dir, "boston-house-prices", "housing.csv")
airline_data_path = os.path.join(data_dir, "airline-flight-data", "airlines_flights_data.csv")

house_agent = HousePrince(house_data_path)
airline_agent = AirlineFlights(airline_data_path)

@tool
def query_boston_house_prices(query: str) -> str:
    """Query the Boston House Prices dataset using pandas query syntax.
    
    Available columns: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV
    
    Examples:
    - "RM > 7 and MEDV > 30" - Find houses with more than 7 rooms and median value > $30k
    - "CHAS == 1" - Find properties near Charles River
    - "CRIM < 1 and MEDV > 25" - Find low crime areas with high property values
    
    Args:
        query: A pandas query string to filter the data
    
    Returns:
        Query results as a string representation of the filtered dataframe
    """
    try:
        result = house_agent.query_data(query)
        if isinstance(result, str):
            return result
        return result.to_string()
    except Exception as e:
        return f"Error querying Boston house prices: {e}"

@tool
def query_airline_flights(query: str) -> str:
    """Query the Airline Flights dataset using pandas query syntax.
    
    Available columns: index, airline, flight, source_city, departure_time, stops, 
    arrival_time, destination_city, class, duration, days_left, price
    
    Examples:
    - "airline == 'SpiceJet' and class == 'Economy'" - Find SpiceJet economy flights
    - "source_city == 'Delhi' and destination_city == 'Mumbai'" - Find Delhi to Mumbai flights
    - "price < 10000 and duration < 3" - Find cheap short flights
    - "stops == 'zero' and class == 'Business'" - Find direct business class flights
    
    Args:
        query: A pandas query string to filter the data
    
    Returns:
        Query results as a string representation of the filtered dataframe
    """
    try:
        result = airline_agent.query_data(query)
        if isinstance(result, str):
            return result
        return result.to_string()
    except Exception as e:
        return f"Error querying airline flights: {e}"

@tool
def get_airline_summary() -> str:
    """Get a summary of all airlines and their flight counts in the dataset.
    
    Returns:
        A summary showing each airline and number of flights
    """
    try:
        result = airline_agent.get_airline_summary()
        return f"Airline Summary:\n{result.to_string()}"
    except Exception as e:
        return f"Error getting airline summary: {e}"

@tool
def get_airline_price_stats(airline: str = "") -> str:
    """Get price statistics for flights, optionally filtered by specific airline.
    
    Args:
        airline: Optional airline name to filter by (e.g., 'SpiceJet', 'Vistara', 'Air_India')
    
    Returns:
        Price statistics including mean, median, min, max, etc.
    """
    try:
        if airline:
            result = airline_agent.get_price_statistics(airline)
        else:
            result = airline_agent.get_price_statistics()
        return f"Price Statistics{' for ' + airline if airline else ''}:\n{result.to_string()}"
    except Exception as e:
        return f"Error getting price statistics: {e}"

@tool
def get_popular_routes() -> str:
    """Get the top 10 most popular flight routes in the dataset.
    
    Returns:
        List of popular routes with their frequencies
    """
    try:
        result = airline_agent.get_routes_summary()
        return f"Top 10 Popular Routes:\n{result.to_string()}"
    except Exception as e:
        return f"Error getting popular routes: {e}"

@tool
def get_house_price_stats() -> str:
    """Get basic statistics about the Boston house prices dataset.
    
    Returns:
        Dataset statistics including column descriptions and basic stats
    """
    try:
        if house_agent.data is not None:
            stats = house_agent.data.describe()
            return f"Boston House Prices Dataset Statistics:\n{stats.to_string()}"
        return "House price data is not loaded"
    except Exception as e:
        return f"Error getting house price statistics: {e}"

# List of all available tools
multi_agent_tools = [
    query_boston_house_prices,
    query_airline_flights,
    get_airline_summary,
    get_airline_price_stats,
    get_popular_routes,
    get_house_price_stats
]