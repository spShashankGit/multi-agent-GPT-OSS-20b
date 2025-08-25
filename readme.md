# Multi-Agent Data Analysis System

A sophisticated multi-agent system built with LangChain that provides AI-powered analysis of multiple datasets:

1. **Boston House Prices** - 506 property records with 14 features
2. **Airline Flights Data** - 300,000+ flight records across 6 airlines

## Features

- 🤖 **AI-Powered Analysis**: Uses LangChain agents with specialized tools for each dataset
- 🏠 **House Price Analysis**: Query Boston housing data with natural language
- ✈️ **Flight Data Analysis**: Analyze airline flights, routes, prices, and trends
- 🔧 **Flexible Querying**: Support for complex pandas-style queries
- 📊 **Statistical Insights**: Automated summaries and statistical analysis
- 🌐 **Web Search Integration**: Additional context through DuckDuckGo search

## Quick Start

### Prerequisites

1. **LM Studio**: Install and run LM Studio with a compatible model on `http://127.0.0.1:1234`
2. **Python Dependencies**: Install required packages

```bash
pip install -r requirements.txt
```

### Running the System

#### Interactive Mode (Recommended)
```bash
python main.py
```

#### Demo Mode
```bash
python main.py --demo
```

#### Test Tools Only (No LLM required)
```bash
python test_tools.py
```

## Available Datasets

### Boston House Prices Dataset
- **Records**: 506 properties
- **Features**: 14 attributes including crime rate, rooms, median value, etc.
- **Columns**: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV

### Airlines Flights Dataset  
- **Records**: 300,153 flights
- **Airlines**: 6 major airlines (Vistara, Air_India, Indigo, GO_FIRST, AirAsia, SpiceJet)
- **Columns**: airline, flight, source_city, destination_city, class, price, duration, stops, etc.

## Example Queries

### House Price Analysis
- "Find houses with more than 7 rooms and low crime rate"
- "What's the average price of houses near Charles River?"
- "Show me properties with median value over $30,000"

### Flight Analysis
- "Which airline has the cheapest flights to Mumbai?"
- "Show me all direct flights from Delhi to Bangalore"
- "Compare average prices between SpiceJet and Vistara"
- "What are the most popular flight routes?"

## System Architecture

```
+----------------+        +---------------------------------+
|      User      |------->|         Master Agent            |
+----------------+        |     (LangChain ReAct Agent)     |
                          +---------------------------------+
                                      |
      +-------------------------------+--------------------------+
      |                               |                          |
      V                               V                          V
+-----+-------------------+   +-------+-------------------+   +----------+-------------+
| Boston House Price Tool |   |   Airline Flights Tool   |   | Web Search Tool      |
| (Query house prices)    |   |  (Query flight data)     |   | (DuckDuckGo search)  |
+-------------------------+   +-------------------------+   +-------------------------+
          |                          |                          
          V                          V                          
+---------+----------+     +---------+----------+               
|  Boston House CSV  |     |  Airlines CSV      |               
|  and Metadata      |     |  and Metadata      |               
+--------------------+     +--------------------+
```

## LM Studio Setup

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load a compatible model (e.g., GPT-4, Llama, Mistral)
3. Start the local server on port 1234
4. Ensure the API endpoint is accessible at `http://127.0.0.1:1234/v1`

## API Reference

### Available Tools

- `query_boston_house_prices(query)` - Query house price data
- `query_airline_flights(query)` - Query flight data  
- `get_airline_summary()` - Get airline statistics
- `get_house_price_stats()` - Get house price statistics
- `get_popular_routes()` - Get top flight routes
- `get_airline_price_stats(airline)` - Get price analysis by airline

### Data File Locations

- Boston House Prices: `data/boston-house-prices/housing.csv`
- Airlines Flights: `data/airline-flight-data/airlines_flights_data.csv`
- Metadata: Available in corresponding JSON files

## Development

### Project Structure
```
├── agents/
│   ├── house_price.py          # Boston house price agent
│   ├── airline_flights.py      # Airline flights agent  
│   ├── multi_agent_tools.py    # LangChain tools
│   └── master_agent.py         # Legacy master agent
├── data/
│   ├── boston-house-prices/    # House price dataset
│   └── airline-flight-data/    # Flight dataset
├── main.py                     # Main entry point
├── test_tools.py              # Tool testing script
├── demo.py                    # Demo script
└── requirements.txt           # Dependencies
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

## Troubleshooting

**LM Studio Connection Issues**:
- Verify LM Studio is running on port 1234
- Check firewall settings
- Try restarting the LM Studio server

**Data Loading Issues**:
- Ensure CSV files are in correct directories
- Check file permissions
- Verify pandas installation

**Query Errors**:
- Use proper pandas query syntax
- Check column names match dataset
- Escape string values with quotes

## License

This project is open source. See LICENSE file for details.