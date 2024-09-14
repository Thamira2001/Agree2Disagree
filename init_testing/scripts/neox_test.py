import requests

def read_api_token():
    with open('secret.txt', 'r') as file:
        token = file.readline().strip()
    return token

API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neox-20b"
headers = {"Authorization": "Bearer TOKEN"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "How to do some",
})

print(output)