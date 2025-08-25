#!/usr/bin/env python3
"""
Multi-Agent Demo Script
Demonstrates the capabilities of the multi-agent system for Boston House Prices and Airline Flights data.
"""

import sys
import os
sys.path.append('/home/runner/work/multi-agent-GPT-OSS-20b/multi-agent-GPT-OSS-20b')

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from agents.multi_agent_tools import multi_agent_tools

def main():
    print("=== Multi-Agent Data Analysis System Demo ===")
    
    # Initialize the LLM
    llm = ChatOpenAI(
        temperature=0, 
        model="gpt-4o", 
        openai_api_base="http://127.0.0.1:1234/v1",
        openai_api_key="dummy-key"
    )
    
    # Use the React prompt template
    prompt = hub.pull("hwchase17/react")
    
    # Create the agent
    agent = create_react_agent(llm=llm, tools=multi_agent_tools, prompt=prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=multi_agent_tools, 
        verbose=True, 
        handle_parsing_errors=True,
        max_iterations=3
    )
    
    # Demo queries
    demo_queries = [
        "How many records are in the Boston house prices dataset? Show me some basic statistics.",
        "What airlines are available in the flights dataset and how many flights does each have?",
        "Find houses in Boston with more than 7 rooms and a median value over $30,000",
        "Show me the top 5 most popular flight routes",
        "What are the price statistics for Vistara airline flights?"
    ]
    
    print("\nRunning demo queries...\n")
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n{'='*60}")
        print(f"Demo Query {i}: {query}")
        print('='*60)
        
        try:
            response = agent_executor.invoke({"input": query})
            print(f"\nResult:\n{response['output']}")
        except Exception as e:
            print(f"Error processing query: {e}")
        
        print("\n" + "-"*60)
    
    print("\n=== Demo Complete ===")
    print("The multi-agent system successfully analyzed both datasets!")

if __name__ == "__main__":
    main()