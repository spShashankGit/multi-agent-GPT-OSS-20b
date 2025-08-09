# Import necessary components
import os
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from ddgs import DDGS
from langchain import hub

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
# Initialize the tools with their data and metadata paths
brooklyn_tool = BrooklynTaxiTool(metadata_path, data_path)
covid_tool = CovidDataTool(metadata_path, data_path)
correlator_tool = CorrelatorTool()

# Create each worker agent
brooklyn_agent = AgentExecutor(...)  # This agent uses the brooklyn_tool
covid_agent = AgentExecutor(...)      # This agent uses the covid_tool
correlator_agent = AgentExecutor(...) # This agent uses the correlator_tool