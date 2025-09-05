# Multi-Agent GPT System

This repository demonstrates a multi-agent system using LangChain that orchestrates specialized agents to analyze and correlate data from different sources.

## Table of Contents

- [API Configuration](#api-configuration)
- [Architecture](#architecture)
- [Model Context Protocol (MCP) Integration Guide](#model-context-protocol-mcp-integration-guide)
  - [What is MCP?](#what-is-mcp)
  - [Why Use MCP?](#why-use-mcp)
  - [Why Was MCP Created?](#why-was-mcp-created)
  - [Limitations of MCP](#limitations-of-mcp)
  - [Advantages of MCP Technology](#advantages-of-mcp-technology)
  - [Demo and Examples](#demo-and-examples)
  - [MCP Integration with This Multi-Agent System](#mcp-integration-with-this-multi-agent-system)
  - [Getting Started with MCP](#getting-started-with-mcp)

## API Configuration

The system uses a local LM Model API endpoint:

```
LM Model API: http://127.0.0.1:1234

GET /v1/models
POST /v1/chat/completions
POST /v1/completions
POST /v1/embeddings
```

## Architecture

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

# Model Context Protocol (MCP) Integration Guide

## What is MCP?

**Model Context Protocol (MCP)** is an open standard developed by Anthropic that enables secure, controlled connections between AI assistants and external data sources, tools, and services. It provides a standardized way for AI models to access and interact with various resources while maintaining security and user control.

## Why Use MCP?

### Key Advantages:

1. **Standardization**: Provides a unified protocol for AI-tool integration across different platforms and services
2. **Security**: Implements secure connection mechanisms with proper authentication and authorization
3. **Scalability**: Enables easy addition of new tools and data sources without custom integration work
4. **Interoperability**: Works across different AI models and platforms that support the protocol
5. **User Control**: Gives users fine-grained control over what data and tools AI assistants can access
6. **Simplified Development**: Reduces complexity in building AI applications that need external tool access

### Use Cases for MCP:

- **Data Integration**: Connect AI to databases, APIs, and file systems
- **Tool Orchestration**: Enable AI to use external tools like calculators, code runners, or specialized software
- **Enterprise Integration**: Safely connect AI to enterprise systems and workflows
- **Research Applications**: Access scientific databases, academic resources, and research tools
- **Development Workflows**: Integrate with IDEs, version control, testing frameworks

## Why Was MCP Created?

MCP was created to address several critical challenges in AI development:

1. **Fragmentation**: Before MCP, each AI application required custom integrations for external tools
2. **Security Concerns**: No standardized way to safely connect AI to sensitive data sources
3. **Development Overhead**: High cost and complexity of building custom tool integrations
4. **Inconsistent User Experience**: Different tools had different ways of working with AI
5. **Scalability Issues**: Difficulty in adding new capabilities to existing AI systems

## Limitations of MCP

### Current Limitations:

1. **Adoption**: Still relatively new, limited ecosystem of MCP-compatible tools
2. **Complexity**: Can be complex to implement for simple use cases
3. **Performance Overhead**: Additional protocol layer may introduce latency
4. **Learning Curve**: Developers need to learn the MCP specification and implementation patterns
5. **Dependency**: Requires both AI models and tools to support the protocol
6. **Infrastructure Requirements**: May require additional infrastructure for hosting MCP servers

### When NOT to Use MCP:

- **Simple, Static Applications**: When you only need basic, unchanging functionality
- **Prototype/MVP Development**: For rapid prototyping where speed is more important than standardization
- **Legacy System Constraints**: When working with systems that cannot be modified to support MCP
- **Limited Resources**: When the overhead of implementing MCP is not justified by the benefits

## Advantages of MCP Technology

### Technical Benefits:

1. **Protocol Standardization**: Consistent interface across all integrations
2. **Security Framework**: Built-in authentication, authorization, and sandboxing
3. **Extensibility**: Easy to add new capabilities without changing core code
4. **Modularity**: Clean separation between AI logic and external tool access
5. **Debugging Support**: Standardized logging and error handling

### Business Benefits:

1. **Reduced Development Costs**: Reusable integrations across multiple AI applications
2. **Faster Time-to-Market**: Standard protocol means faster implementation
3. **Better Maintenance**: Centralized management of tool integrations
4. **Enhanced Security**: Standardized security practices across all integrations
5. **Vendor Independence**: Not locked into specific AI platforms or tool providers

## Demo and Examples

### Official MCP Resources:

- **GitHub Repository**: [https://github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)
- **Specification**: [MCP Specification](https://spec.modelcontextprotocol.io/)
- **Example Implementations**: Available in the official GitHub repository
- **Tool Registry**: Community-maintained list of MCP-compatible tools

### Sample MCP Integration:

```python
# Example of MCP client integration (conceptual)
from mcp import Client, Tool

# Connect to MCP server
client = Client("mcp://localhost:8080")

# List available tools
tools = client.list_tools()

# Use a specific tool
calculator = client.get_tool("calculator")
result = calculator.invoke("add", {"a": 5, "b": 3})
```

## MCP Integration with This Multi-Agent System

### Can This Multi-Agent System Run on MCP?

**Yes, this multi-agent system can be adapted to run with MCP.** Here's how:

#### Current Architecture:
- **Direct Dependencies**: LangChain, DDGS, local file access, OpenAI API
- **Tight Coupling**: Agents directly access data sources and tools
- **Limited Scalability**: Adding new tools requires code modification

#### MCP-Enhanced Architecture:
```
+----------------+     MCP     +---------------------------------+
|      User      |<----------->|         Master Agent            |
+----------------+             |     (Orchestrates via MCP)      |
                               +---------------------------------+
                                           |
                           MCP Protocol    |    MCP Protocol
                                           |
      +------------------------------------+---------------------------+
      |                                    |                           |
      V                                    V                           V
+-----+-------------------+     +----------+----------------+     +----+-----------------+
| Brooklyn Data MCP Server|     |   COVID Data MCP Server  |     | Analytics MCP Server |
| (Serves Brooklyn data)  |     |  (Serves COVID data)     |     | (Analysis tools)     |
+-------------------------+     +---------------------------+     +----------------------+
          |                               |                               |
          V                               V                               V
+---------+----------+           +---------+----------+           +-------+--------+
|  Brooklyn Taxi CSV |           |  COVID Data CSV    |           | Correlation    |
|  and Metadata      |           |  and Metadata      |           | Algorithms     |
+--------------------+           +--------------------+           +----------------+
```

### Current State:

This multi-agent system currently uses direct integrations with:
- LangChain framework
- DuckDuckGo search (DDGS)
- Local CSV data sources
- OpenAI-compatible API endpoints

### Potential MCP Integration:

#### 1. **Data Source Integration**
```python
# Replace direct file access with MCP data sources
brooklyn_tool = MCPDataTool("mcp://brooklyn-taxi-server")
covid_tool = MCPDataTool("mcp://covid-data-server")
```

#### 2. **Tool Standardization**
```python
# Standardize search and analysis tools via MCP
search_tool = MCPTool("mcp://search-server")
analytics_tool = MCPTool("mcp://analytics-server")
```

#### 3. **Enhanced Security**
- Secure access to sensitive datasets
- Controlled permissions for each agent
- Audit trails for all data access

#### 4. **Scalability Improvements**
- Easy addition of new data sources
- Dynamic tool discovery
- Horizontal scaling of tool servers

### Migration Path:

1. **Phase 1**: Wrap existing tools in MCP servers
   ```python
   # Create MCP server for existing data sources
   @mcp_server.tool("brooklyn_taxi_query")
   async def brooklyn_taxi_query(query: str) -> str:
       # Existing brooklyn taxi logic here
       return query_brooklyn_data(query)
   ```

2. **Phase 2**: Replace direct integrations with MCP clients
   ```python
   # Replace direct imports with MCP clients
   class MCPAgent:
       def __init__(self, mcp_server_url: str):
           self.client = MCPClient(mcp_server_url)
           
       async def query_data(self, query: str):
           return await self.client.call_tool("data_query", {"query": query})
   ```

3. **Phase 3**: Add new MCP-native capabilities
   - Real-time data streaming
   - Advanced analytics tools
   - External API integrations

4. **Phase 4**: Implement advanced MCP features
   - Resource management
   - Multi-tenant access control
   - Performance monitoring

### Implementation Example:

```python
# MCP-enabled master agent
from mcp import Client, Server
import asyncio

class MCPMasterAgent:
    def __init__(self):
        self.data_clients = {
            'brooklyn': Client('mcp://brooklyn-server:8080'),
            'covid': Client('mcp://covid-server:8081'),
            'analytics': Client('mcp://analytics-server:8082')
        }
    
    async def orchestrate_analysis(self, user_query: str):
        # Get Brooklyn taxi data via MCP
        brooklyn_data = await self.data_clients['brooklyn'].call_tool(
            'query_data', {'query': user_query}
        )
        
        # Get COVID data via MCP
        covid_data = await self.data_clients['covid'].call_tool(
            'query_data', {'query': user_query}
        )
        
        # Perform correlation analysis via MCP
        correlation = await self.data_clients['analytics'].call_tool(
            'correlate', {
                'data1': brooklyn_data,
                'data2': covid_data
            }
        )
        
        return correlation
```

### Benefits for This System:

- **Easier Data Source Management**: Add new datasets without code changes
- **Better Security**: Controlled access to sensitive data
- **Enhanced Monitoring**: Standardized logging and metrics
- **Improved Collaboration**: Other teams can easily integrate with your data sources
- **Future-Proofing**: Compatibility with emerging MCP ecosystem
- **Dynamic Scaling**: Scale individual components independently
- **Service Isolation**: Failures in one service don't affect others

## Getting Started with MCP

1. **Learn the Specification**: Review the MCP specification documentation
2. **Try Examples**: Clone and run official MCP examples
3. **Start Small**: Begin with simple tool integrations
4. **Build Incrementally**: Gradually migrate existing integrations to MCP
5. **Join the Community**: Participate in MCP community discussions and development

---

*For more information about MCP, visit the [official documentation](https://spec.modelcontextprotocol.io/) and [GitHub repository](https://github.com/modelcontextprotocol).*