#!/usr/bin/env python3
"""
Validation script for multi-agent system components
This script tests all components without requiring LLM/external dependencies
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_data_loading():
    """Test that both datasets load correctly."""
    print("Testing data loading...")
    
    from agents.house_price import HousePrince
    from agents.airline_flights import AirlineFlights
    
    # Test house price agent
    house_agent = HousePrince("data/boston-house-prices/housing.csv")
    assert house_agent.data is not None, "House price data failed to load"
    assert house_agent.data.shape[0] > 0, "House price data is empty"
    print(f"✅ House price data: {house_agent.data.shape[0]} records")
    
    # Test airline agent
    airline_agent = AirlineFlights("data/airline-flight-data/airlines_flights_data.csv")
    assert airline_agent.data is not None, "Airline data failed to load"
    assert airline_agent.data.shape[0] > 0, "Airline data is empty"
    print(f"✅ Airline data: {airline_agent.data.shape[0]} records")

def test_queries():
    """Test query functionality."""
    print("\nTesting query functionality...")
    
    from agents.house_price import HousePrince
    from agents.airline_flights import AirlineFlights
    
    house_agent = HousePrince("data/boston-house-prices/housing.csv")
    airline_agent = AirlineFlights("data/airline-flight-data/airlines_flights_data.csv")
    
    # Test house price queries
    result = house_agent.query_data("RM > 6")
    assert not isinstance(result, str) or "error" not in result.lower(), "House price query failed"
    print("✅ House price queries working")
    
    # Test airline queries
    result = airline_agent.query_data("airline == 'SpiceJet'")
    assert not isinstance(result, str) or "error" not in result.lower(), "Airline query failed"
    print("✅ Airline queries working")

def test_tools():
    """Test LangChain tools."""
    print("\nTesting LangChain tools...")
    
    from agents.multi_agent_tools import (
        query_boston_house_prices,
        query_airline_flights, 
        get_airline_summary,
        get_house_price_stats
    )
    
    # Test house price tool
    result = query_boston_house_prices.invoke({"query": "RM > 7"})
    assert "error" not in result.lower(), "House price tool failed"
    print("✅ House price tool working")
    
    # Test airline tool
    result = query_airline_flights.invoke({"query": "airline == 'SpiceJet'"})
    assert "error" not in result.lower(), "Airline tool failed"
    print("✅ Airline tool working")
    
    # Test summary tools
    result = get_airline_summary.invoke({})
    assert "error" not in result.lower(), "Airline summary tool failed"
    print("✅ Airline summary tool working")
    
    result = get_house_price_stats.invoke({})
    assert "error" not in result.lower(), "House price stats tool failed"
    print("✅ House price stats tool working")

def test_data_integrity():
    """Test data integrity and expected content."""
    print("\nTesting data integrity...")
    
    from agents.house_price import HousePrince
    from agents.airline_flights import AirlineFlights
    
    house_agent = HousePrince("data/boston-house-prices/housing.csv")
    airline_agent = AirlineFlights("data/airline-flight-data/airlines_flights_data.csv")
    
    # Test house data structure
    expected_house_cols = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    assert all(col in house_agent.data.columns for col in expected_house_cols), "House data missing expected columns"
    print("✅ House data has expected columns")
    
    # Test airline data structure
    expected_airline_cols = ['airline', 'source_city', 'destination_city', 'price']
    assert all(col in airline_agent.data.columns for col in expected_airline_cols), "Airline data missing expected columns"
    print("✅ Airline data has expected columns")
    
    # Test airline counts
    airlines = airline_agent.data['airline'].unique()
    assert len(airlines) >= 5, f"Expected at least 5 airlines, got {len(airlines)}"
    print(f"✅ Found {len(airlines)} airlines")

def main():
    """Run all validation tests."""
    print("=" * 60)
    print("MULTI-AGENT SYSTEM VALIDATION")
    print("=" * 60)
    
    try:
        test_data_loading()
        test_queries()
        test_tools()
        test_data_integrity()
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED!")
        print("✅ Multi-agent system is working correctly")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ VALIDATION FAILED: {e}")
        print("=" * 60)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)