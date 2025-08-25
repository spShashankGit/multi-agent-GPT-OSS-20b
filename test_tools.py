#!/usr/bin/env python3
"""
Simple test of the multi-agent system without LLM dependency
"""

import sys
import os
sys.path.append('/home/runner/work/multi-agent-GPT-OSS-20b/multi-agent-GPT-OSS-20b')

from agents.multi_agent_tools import (
    query_boston_house_prices, 
    query_airline_flights,
    get_airline_summary,
    get_house_price_stats,
    get_popular_routes
)

def test_multi_agent_tools():
    print("=== Multi-Agent System Test (Without LLM) ===\n")
    
    # Test 1: House price statistics
    print("1. Boston House Price Dataset Statistics:")
    result = get_house_price_stats.invoke({})
    print(result[:300] + "...\n" if len(result) > 300 else result + "\n")
    
    # Test 2: Airline summary
    print("2. Airline Summary:")
    result = get_airline_summary.invoke({})
    print(result + "\n")
    
    # Test 3: House price query
    print("3. Houses with more than 7 rooms and high value:")
    result = query_boston_house_prices.invoke({"query": "RM > 7 and MEDV > 30"})
    print(f"Found {len(result.split('\\n')) - 1} matching properties\n")
    
    # Test 4: Airline query
    print("4. SpiceJet flights from Delhi:")
    result = query_airline_flights.invoke({"query": "airline == 'SpiceJet' and source_city == 'Delhi'"})
    lines = result.split('\n')
    print(f"Found {len(lines) - 1} SpiceJet flights from Delhi")
    print("Sample flights:")
    for line in lines[1:4]:  # Show first 3 results
        if line.strip():
            print(f"  {line}")
    print()
    
    # Test 5: Popular routes
    print("5. Most Popular Flight Routes:")
    result = get_popular_routes.invoke({})
    print(result)
    
    print("\n=== All Tools Working Successfully! ===")

if __name__ == "__main__":
    test_multi_agent_tools()