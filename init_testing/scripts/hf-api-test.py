import os
from dotenv import load_dotenv
from pathlib import Path
import requests
# from langchain import HuggingFaceHub

 
# Load environment variables from the .env file
dotenv_path = Path('../../.env')
load_dotenv(dotenv_path=dotenv_path)

# Access the API token from the environment variables
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

print(api_token) #check if .env file is importing the access token for huging face hub properly 

headers = {"Authorization": f"Bearer {api_token}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"

def query_huggingface_api(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

input_text = "can you tell who lebron james is ?"
response = query_huggingface_api({"inputs": input_text})

print(response)



