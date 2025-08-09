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