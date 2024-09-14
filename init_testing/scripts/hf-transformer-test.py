import os
from dotenv import load_dotenv
from pathlib import Path
import requests

token_path = 'secret.txt'

def read_api_token():
    try:
        with open(token_path, 'r') as file:
            token = file.readline().strip()
        return token
    except FileNotFoundError:
        print("Token file not found.")
        return None

# Load environment variables from the .env file
dotenv_path = Path('../../.env')
load_dotenv(dotenv_path)

api_token = read_api_token()

if api_token:
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b"

    def query_huggingface_api(payload):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    input_text = "can you tell who lebron james is ?"
    response = query_huggingface_api({"inputs": input_text})

    if response:
        print(response)
else:
    print("API token is missing.")
