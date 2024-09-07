import openai

# Load the API key from secret.txt
with open('secret.txt', 'r') as file:
    api_key = file.read().strip()

# Set your API key
openai.api_key = api_key

# Make a sample API call
response = openai.ChatCompletion.create(
    model="gpt-4",  # or "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Give me a summary of the latest AI research."}
    ]
)

# Print the response
print(response['choices'][0]['message']['content'])
