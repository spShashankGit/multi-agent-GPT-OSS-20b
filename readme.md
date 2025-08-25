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

# Architecture Approaches

This repository demonstrates both multi-agent and multi-tool patterns. For detailed guidance on when to choose each approach, see [ARCHITECTURE_GUIDE.md](ARCHITECTURE_GUIDE.md).

## Multi-Agent Approach (Demonstrated)

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

**Use when**: Multiple specialized domains, independent processing, team boundaries

## Multi-Tool Approach (Demonstrated)

```
+----------------+        +-------------------+
|      User      |------->|   Single Agent    |
+----------------+        |                   |
                          +-------------------+
                                    |
                    +---------------+---------------+
                    |               |               |
                    V               V               V
            +-------+-------+ +-----+-----+ +-------+-------+
            | Search Tool   | | Data Tool | | Analysis Tool |
            +---------------+ +-----------+ +---------------+
```

**Use when**: Single domain focus, sequential processing, simple coordination

## Quick Decision Guide

- **Multi-Agent**: 3+ domains, 3+ teams, parallel processing needs
- **Multi-Tool**: 1 domain, 1-2 developers, sequential tasks

### 🛠️ Interactive Decision Helper

Run the interactive decision helper to get personalized recommendations:

```bash
python architecture_decision_helper.py
```

This tool will ask about your specific requirements and provide scored recommendations with detailed reasoning.

### 📖 Detailed Documentation

- **🚀 Quick Reference**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Decision matrix and thresholds
- **📋 Comprehensive Guide**: [ARCHITECTURE_GUIDE.md](ARCHITECTURE_GUIDE.md) - Detailed criteria, examples, and best practices