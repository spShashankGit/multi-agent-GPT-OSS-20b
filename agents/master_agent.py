# Import necessary components
import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from ddgs import DDGS
from langchain import hub

"""
ARCHITECTURE DECISION EXAMPLE:

This file demonstrates BOTH multi-agent and multi-tool patterns to illustrate 
when each approach is appropriate. See ARCHITECTURE_GUIDE.md for detailed guidance.

MULTI-TOOL EXAMPLE (Lines 18-67):
- Single agent with DuckDuckGo search tool
- WHY: Simple task (answer questions), sequential processing, single domain
- USE CASE: Quick queries that need web search capability

MULTI-AGENT EXAMPLE (Lines 70-79): 
- Master agent orchestrating specialized data agents
- WHY: Multiple domains (taxi, health, statistics), independent processing, specialized expertise
- USE CASE: Complex data analysis requiring domain-specific agents
"""

# ------------------
# MULTI-TOOL ARCHITECTURE EXAMPLE  
# ------------------
# This section demonstrates when to use a single agent with multiple tools
# Decision factors that led to multi-tool choice:
# ✓ Single domain: web search and question answering
# ✓ Sequential processing: search then format response
# ✓ Simple tool interface with shared context
# ✓ Low complexity task suitable for single agent
# ✓ Rapid prototyping and development simplicity

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

tools = [
    ddg_search_tool
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

# 6. Run the Agent with a "Hello World" question
# This is a task that the agent cannot solve with just its internal knowledge.
# It MUST use the web search tool to find the answer.
response = agent_executor.invoke({"input": "What is the weather in Paris right now?"})

# 7. Print the final answer
print("\n--- Final Response ---")
print(response["output"])


# ------------------
# MULTI-AGENT ARCHITECTURE EXAMPLE
# ------------------
# This section demonstrates when to use multiple specialized agents
# Decision factors that led to multi-agent choice:
# ✓ 3 distinct domains: transportation data, health data, statistical analysis  
# ✓ Independent data sources with different formats and processing needs
# ✓ Parallel processing opportunities (agents can work simultaneously)
# ✓ Clear separation of concerns and expertise boundaries
# ✓ Different computational requirements per domain

# Initialize the tools with their data and metadata paths
brooklyn_tool = BrooklynTaxiTool(metadata_path, data_path)
covid_tool = CovidDataTool(metadata_path, data_path)
correlator_tool = CorrelatorTool()

# Create each worker agent with specialized capabilities
brooklyn_agent = AgentExecutor(...)  # This agent uses the brooklyn_tool
covid_agent = AgentExecutor(...)      # This agent uses the covid_tool
correlator_agent = AgentExecutor(...) # This agent uses the correlator_tool