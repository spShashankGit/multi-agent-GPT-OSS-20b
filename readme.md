# Multi-Agent GPT OSS 20b

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

## 🔒 Security Notice

This repository now includes comprehensive **prompt injection protection**. Please see:
- [**PROMPT_INJECTION_GUIDE.md**](PROMPT_INJECTION_GUIDE.md) - Educational guide about prompt injection
- [**SECURITY_README.md**](SECURITY_README.md) - How to use the security features
- [**prompt_injection_demo.py**](prompt_injection_demo.py) - Interactive security demonstration

**Quick security check:**
```python
from security_utils import is_input_safe
if is_input_safe(user_input):
    # Process safely
    pass
```

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