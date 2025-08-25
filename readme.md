```
LM Model API: http://127.0.0.1:1234

GET
/v1/models

POST
/v1/chat/completions

POST
/v1/completions

POST
/v1/embeddings

```

# Multi-Agent GPT System

This repository implements a multi-agent system using LangChain and local LLM models. The system demonstrates various AI response frameworks and agent coordination patterns.

## Documentation

📖 **[OpenAI Harmony Response Framework](docs/harmony-framework.md)** - Comprehensive guide to the Harmony framework for structured AI interactions, including when to use it, alternatives, and implementation examples.

🔧 **[Harmony Integration Example](examples/harmony_integration.py)** - Working code example showing how to integrate Harmony framework with the existing multi-agent system.

## Architecture

# First approach

```
+----------------+        +---------------------------------+
|      User      |------->|         Master Agent            |
+----------------+        |     (Orchestrates the plan)     |
                          +---------------------------------+
                                      |
      +-------------------------------+--------------------------+
      |                               |                          |
      V                               V                          V
+-----+-------------------+   +-------+-------------------+   +----------+-------------+
| Brooklyn Taxi Data Agent|-->|   COVID Data Agent      |-->| Data Analyst Agent   |
| (Queries Brooklyn data) |   |  (Queries COVID data)   |   | (Calculates correlation)|
+-------------------------+   +-------------------------+   +-------------------------+
          |                          |                          ^
          V                          V                          |
+---------+----------+     +---------+----------+               |
|  Brooklyn Taxi CSV |     |  COVID Data CSV    |---------------|
|  and Metadata      |     |  and Metadata      |---------------|
+--------------------+     +--------------------+
```

## Response Frameworks

This system currently uses the **ReAct** (Reasoning + Acting) pattern from LangChain for agent coordination. The ReAct pattern follows a Thought → Action → Observation loop that allows agents to reason about their actions before executing them.

### Framework Comparison

For complex multi-agent systems like this one, consider these response frameworks:

- **ReAct** (Current): Good for sequential reasoning and tool usage
- **OpenAI Harmony**: Excellent for structured, multi-tool applications with transparency requirements
- **Function Calling**: Suitable for simple tool integration scenarios
- **Plan-and-Execute**: Better for complex project management tasks

See the [Harmony Framework documentation](docs/harmony-framework.md) for detailed comparisons and implementation guidance.

## Getting Started

1. Ensure you have LM Studio running locally at `http://127.0.0.1:1234`
2. Install dependencies: `pip install -r requirements.txt` (if available)
3. Run the agents from the `agents/` directory
4. Explore different response frameworks based on your use case requirements

### Examples

- **Harmony Integration**: Run `python examples/harmony_integration.py` to see how the Harmony framework structures multi-agent interactions
- **Basic Agent**: Try `python agents/hello-world.py` for a simple LLM interaction
- **Data Analysis**: Explore `python agents/house_price.py` for dataset querying capabilities