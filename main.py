#!/usr/bin/env python3
"""
Multi-Agent Data Analysis System
================================

This script demonstrates a multi-agent system that can analyze:
1. Boston House Prices dataset (506 records with 14 features)
2. Airlines Flights dataset (300K+ records across 6 airlines)

The system uses LangChain agents with specialized tools for each dataset,
providing an AI-powered interface for data analysis and querying.

Usage:
    python main.py [--demo]
    
    --demo: Run a predefined demo without interactive mode
"""

import sys
import os
import argparse
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from agents.multi_agent_tools import multi_agent_tools

def create_multi_agent_system():
    """Initialize and return the multi-agent system."""
    
    # Initialize the LLM (assumes LM Studio or compatible API running locally)
    llm = ChatOpenAI(
        temperature=0, 
        model="gpt-4o", 
        openai_api_base="http://127.0.0.1:1234/v1",
        openai_api_key="dummy-key"
    )
    
    # Use the React prompt template for reasoning
    prompt = hub.pull("hwchase17/react")
    
    # Create the agent with multi-dataset tools
    agent = create_react_agent(llm=llm, tools=multi_agent_tools, prompt=prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=multi_agent_tools, 
        verbose=True, 
        handle_parsing_errors=True,
        max_iterations=3
    )
    
    return agent_executor

def run_demo(agent_executor):
    """Run a series of demo queries to showcase the system."""
    
    demo_queries = [
        {
            "query": "How many records are in each dataset? Give me basic statistics for both.",
            "description": "Dataset Overview"
        },
        {
            "query": "What airlines are in the flights dataset and how many flights does each have?",
            "description": "Airlines Analysis"
        },
        {
            "query": "Find all properties in Boston with more than 7 rooms and median value over $30,000. How many are there?",
            "description": "High-Value Properties"
        },
        {
            "query": "What are the top 5 most popular flight routes?",
            "description": "Popular Routes"
        },
        {
            "query": "Compare the average prices between SpiceJet and Vistara airlines",
            "description": "Airline Price Comparison"
        },
        {
            "query": "Find all direct flights (zero stops) from Delhi to Mumbai. Which airline has the most?",
            "description": "Direct Flights Analysis"
        }
    ]
    
    print("=" * 80)
    print("MULTI-AGENT DATA ANALYSIS SYSTEM DEMO")
    print("=" * 80)
    print("This demo showcases AI-powered analysis of:")
    print("• Boston House Prices (506 properties, 14 features)")
    print("• Airlines Flights (300K+ flights, 6 airlines)")
    print("=" * 80)
    
    for i, demo in enumerate(demo_queries, 1):
        print(f"\n{'#' * 10} Demo {i}: {demo['description']} {'#' * 10}")
        print(f"Query: {demo['query']}")
        print("-" * 60)
        
        try:
            response = agent_executor.invoke({"input": demo['query']})
            print(f"Result:\n{response['output']}")
        except Exception as e:
            print(f"Error: {e}")
            print("This might be due to LM Studio not running or network issues.")
        
        print("-" * 60)
        input("Press Enter to continue to next demo...")
    
    print(f"\n{'=' * 80}")
    print("DEMO COMPLETE!")
    print("=" * 80)

def run_interactive(agent_executor):
    """Run interactive mode where users can ask their own questions."""
    
    print("=" * 80)
    print("MULTI-AGENT DATA ANALYSIS SYSTEM - INTERACTIVE MODE")
    print("=" * 80)
    print("Ask questions about:")
    print("🏠 Boston House Prices - Use column names: CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV")
    print("✈️  Airline Flights - Use column names: airline, flight, source_city, destination_city, class, price, duration, stops")
    print()
    print("Example queries:")
    print("• 'Find houses near Charles River with crime rate less than 1'")
    print("• 'Show me all business class flights from Delhi to Bangalore'")
    print("• 'What's the average house price for properties with more than 6 rooms?'")
    print("• 'Which airline has the cheapest flights to Mumbai?'")
    print()
    print("Type 'quit', 'exit', or 'q' to stop")
    print("=" * 80)
    
    while True:
        try:
            user_input = input("\n🤖 Ask your question: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q', '']:
                print("👋 Goodbye!")
                break
                
            print(f"\n🔍 Processing: {user_input}")
            print("-" * 60)
            
            response = agent_executor.invoke({"input": user_input})
            print(f"📊 Result:\n{response['output']}")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Tip: Make sure LM Studio is running on http://127.0.0.1:1234")
            print("Or try rephrasing your question.")

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent Data Analysis System")
    parser.add_argument("--demo", action="store_true", help="Run demo mode")
    args = parser.parse_args()
    
    try:
        print("🚀 Initializing Multi-Agent System...")
        agent_executor = create_multi_agent_system()
        print("✅ System ready!")
        
        if args.demo:
            run_demo(agent_executor)
        else:
            run_interactive(agent_executor)
            
    except Exception as e:
        print(f"❌ Failed to initialize system: {e}")
        print("\n💡 Troubleshooting:")
        print("1. Make sure LM Studio is running on http://127.0.0.1:1234")
        print("2. Check that all dependencies are installed: pip install -r requirements.txt")
        print("3. Verify data files are in the correct locations")
        sys.exit(1)

if __name__ == "__main__":
    main()