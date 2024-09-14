import os
from dotenv import load_dotenv
from pathlib import Path
import requests

token_path = 'secret.txt'

def read_api_token():
    with open(token_path, 'r') as file:
        token = file.readline().strip()
    return token

# from langchain import HuggingFaceHub

 
# Load environment variables from the .env file
dotenv_path = Path('../../.env')
load_dotenv(dotenv_path=dotenv_path)

api_token = read_api_token()
#check if .env file is importing the access token for huging face hub properly 

headers = {"Authorization": f"Bearer {api_token}"}
API_URL = "https://api-inference.huggingface.co/models/Reflection-Llama-3.1-70B"

def query_huggingface_api(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

input_text = "can you tell who lebron james is ?"
response = query_huggingface_api({"inputs": input_text})

print(response)



