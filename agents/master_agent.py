# Import necessary components
import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from ddgs import DDGS
from langchain import hub
from multi_agent_tools import multi_agent_tools

# 1. Define the LLM (Large Language Model)
# We instantiate the LLM. The agent will use this model for reasoning.
llm = ChatOpenAI(temperature=0, 
                 model="gpt-4o", 
                 openai_api_base="http://127.0.0.1:1234/v1",
                 openai_api_key="dummy-key")

# 2. Define a custom tool for the DDGS library
# The `@tool` decorator makes a regular Python function into a LangChain tool.
@tool
def ddg_search_tool(query: str) -> str:
    """Performs a search on DuckDuckGo and returns the results.
    The input to this tool is a string search query."""
    with DDGS() as ddgs:
        # Pass the query as the first positional argument
        results = ddgs.text(query, max_results=5)
        # The rest of your code is fine
        formatted_results = "\n\n".join(
            [f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}" for r in results]
        )
    return formatted_results

# Combine web search with multi-agent data tools
tools = [
    ddg_search_tool,
    *multi_agent_tools  # Add all the data analysis tools
]

# 3. Define the Agent's Prompt
# We use a pre-built prompt from LangChain's 'hub'. This prompt tells the LLM how to act as an agent.
# It includes instructions on how to use the tools and how to format its thoughts and actions.
prompt = hub.pull("hwchase17/react")

# 4. Create the Agent
# We create the agent by combining the LLM, the tools, and the prompt.
# This gives the LLM the ability to "see" the tools and decide when to use them.
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# 5. Create the Agent Executor
# The AgentExecutor is the "runtime" for the agent.
# It's responsible for managing the agent's thought-process loop:
# - It gives the prompt and tools to the LLM.
# - The LLM decides what to do (e.g., use the search tool).
# - The Executor executes the tool's action.
# - The Executor feeds the tool's result back to the LLM.
# - This loop continues until the LLM decides it has a final answer.
# Thought, action, observation
agent_executor = AgentExecutor(agent=agent, 
                               tools=tools, 
                               verbose=True, 
                               handle_parsing_errors=True,
                               max_iterations=2)

# 6. Multi-Agent Data Analysis Demo
# This demonstrates the multi-agent system analyzing both datasets
if __name__ == "__main__":
    print("=== Multi-Agent Data Analysis System ===")
    print("Available capabilities:")
    print("1. Boston House Prices Analysis")
    print("2. Airline Flights Data Analysis")
    print("3. Web Search for additional context")
    print()
    
    # Example queries for different data analysis scenarios
    sample_queries = [
        "Find the average price of houses near the Charles River (CHAS == 1) in the Boston dataset",
        "What are the top 3 most expensive airlines by average ticket price?",
        "Show me all direct flights (zero stops) from Delhi to Mumbai",
        "Find properties in Boston with more than 7 rooms and low crime rate (CRIM < 1)"
    ]
    
    print("Sample queries you can ask:")
    for i, query in enumerate(sample_queries, 1):
        print(f"{i}. {query}")
    
    print("\n" + "="*50)
    print("Starting interactive mode...")
    print("Type 'quit' to exit")
    print("="*50 + "\n")
    
    while True:
        user_input = input("Ask a question about Boston house prices or airline flights: ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
            
        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"\n--- Response ---")
            print(response["output"])
            print("\n" + "-"*50 + "\n")
        except Exception as e:
            print(f"Error: {e}")
            print("Please try rephrasing your question.\n")


# Legacy code kept for reference - but now we have a proper multi-agent system above
# ------------------
# Initialize the tools with their data and metadata paths
# brooklyn_tool = BrooklynTaxiTool(metadata_path, data_path)
# covid_tool = CovidDataTool(metadata_path, data_path)
# correlator_tool = CorrelatorTool()

# Create each worker agent
# brooklyn_agent = AgentExecutor(...)  # This agent uses the brooklyn_tool
# covid_agent = AgentExecutor(...)      # This agent uses the covid_tool
# correlator_agent = AgentExecutor(...) # This agent uses the correlator_tool