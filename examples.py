#!/usr/bin/env python3
"""
Multi-Agent System Examples
===========================

This script demonstrates specific use cases for the multi-agent system
without requiring LLM connectivity, showing direct tool usage.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.multi_agent_tools import (
    query_boston_house_prices,
    query_airline_flights,
    get_airline_summary,
    get_house_price_stats,
    get_popular_routes,
    get_airline_price_stats
)

def example_house_analysis():
    """Example house price analysis scenarios."""
    print("🏠 BOSTON HOUSE PRICE ANALYSIS EXAMPLES")
    print("=" * 50)
    
    # Example 1: High-value properties
    print("1. Properties with more than 7 rooms and high value:")
    result = query_boston_house_prices.invoke({"query": "RM > 7 and MEDV > 25"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} properties matching criteria")
    
    # Example 2: Charles River properties
    print("\n2. Properties near Charles River (CHAS=1):")
    result = query_boston_house_prices.invoke({"query": "CHAS == 1"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} properties near Charles River")
    
    # Example 3: Low crime, high value areas
    print("\n3. Low crime areas with high property values:")
    result = query_boston_house_prices.invoke({"query": "CRIM < 1 and MEDV > 30"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} properties in safe, high-value areas")
    
    # Example 4: Dataset statistics
    print("\n4. Dataset Overview:")
    result = get_house_price_stats.invoke({})
    lines = result.split('\n')
    print(f"   Dataset contains 506 Boston area properties")
    print(f"   Features: Crime rate, Rooms, Age, Distance to employment centers, etc.")

def example_airline_analysis():
    """Example airline analysis scenarios."""
    print("\n✈️ AIRLINE FLIGHTS ANALYSIS EXAMPLES")
    print("=" * 50)
    
    # Example 1: Airlines overview
    print("1. Airlines in the dataset:")
    result = get_airline_summary.invoke({})
    print(result.replace("Airline Summary:\n", "   "))
    
    # Example 2: Popular routes
    print("\n2. Most popular flight routes:")
    result = get_popular_routes.invoke({})
    lines = result.split('\n')[1:6]  # Top 5 routes
    for line in lines:
        if line.strip():
            print(f"   {line}")
    
    # Example 3: SpiceJet flights from Delhi
    print("\n3. SpiceJet flights from Delhi:")
    result = query_airline_flights.invoke({"query": "airline == 'SpiceJet' and source_city == 'Delhi'"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} SpiceJet flights from Delhi")
    
    # Example 4: Business class flights
    print("\n4. Business class flights:")
    result = query_airline_flights.invoke({"query": "class == 'Business'"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} business class flights")
    
    # Example 5: Direct flights Delhi to Mumbai
    print("\n5. Direct flights Delhi to Mumbai:")
    result = query_airline_flights.invoke({"query": "source_city == 'Delhi' and destination_city == 'Mumbai' and stops == 'zero'"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} direct flights on this route")

def example_price_analysis():
    """Example price analysis scenarios."""
    print("\n💰 PRICE ANALYSIS EXAMPLES")
    print("=" * 50)
    
    # Example 1: Vistara price statistics
    print("1. Vistara flight prices:")
    result = get_airline_price_stats.invoke({"airline": "Vistara"})
    lines = result.split('\n')
    for line in lines[1:4]:  # Show first few stats
        if line.strip():
            print(f"   {line}")
    
    # Example 2: Cheap flights
    print("\n2. Budget flights under ₹10,000:")
    result = query_airline_flights.invoke({"query": "price < 10000"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} affordable flights")
    
    # Example 3: Premium flights
    print("\n3. Premium flights over ₹25,000:")
    result = query_airline_flights.invoke({"query": "price > 25000"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} premium flights")

def example_complex_queries():
    """Example complex analysis scenarios."""
    print("\n🔍 COMPLEX ANALYSIS EXAMPLES")
    print("=" * 50)
    
    # Example 1: Short duration business flights
    print("1. Short business flights (under 2 hours):")
    result = query_airline_flights.invoke({"query": "class == 'Business' and duration < 2"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} quick business flights")
    
    # Example 2: Last-minute flights
    print("\n2. Last-minute bookings (1 day left):")
    result = query_airline_flights.invoke({"query": "days_left == 1"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} last-minute flights")
    
    # Example 3: High-end houses with low taxes
    print("\n3. Expensive Boston houses with low tax rates:")
    result = query_boston_house_prices.invoke({"query": "MEDV > 40 and TAX < 300"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} high-value, low-tax properties")
    
    # Example 4: Morning economy flights from Bangalore
    print("\n4. Morning economy flights from Bangalore:")
    result = query_airline_flights.invoke({"query": "source_city == 'Bangalore' and departure_time == 'Morning' and class == 'Economy'"})
    lines = result.split('\n')
    print(f"   Found {max(0, len(lines) - 2)} morning economy departures")

def main():
    """Run all example analyses."""
    print("🤖 MULTI-AGENT SYSTEM - ANALYSIS EXAMPLES")
    print("=" * 60)
    print("Demonstrating real-world use cases for data analysis")
    print("=" * 60)
    
    try:
        example_house_analysis()
        example_airline_analysis() 
        example_price_analysis()
        example_complex_queries()
        
        print("\n" + "=" * 60)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("💡 These queries can be combined with AI for natural language interaction")
        print("🚀 Run 'python main.py' for AI-powered analysis")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()