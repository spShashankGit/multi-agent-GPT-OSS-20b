from openai import OpenAI

# Set the base URL to your LM Studio server
base_url = "http://127.0.0.1:1234/v1"

# Instantiate the OpenAI client
client = OpenAI(api_key="not-needed", base_url=base_url)

# Call the chat completions endpoint using the client object
completion = client.chat.completions.create(
    model="model-identifier-here", # You can put any string here
    messages=[
        {"role": "user", "content": "What is the capital of Germany?"}
    ],
    temperature=0.7
)

# Print the response
print(completion.choices[0].message.content)