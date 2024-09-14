from openai import OpenAI

# Load the API key from secret.txt
with open('init_testing/scripts/secret.txt', 'r') as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)
completion = client.chat.completions.create(
    # model="gpt-4o",
    model="gpt-3.5-turbo-0125",

    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)