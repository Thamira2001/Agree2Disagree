import google.generativeai as genai
import os
import requests

def read_api_token():
    with open('geminai.txt', 'r') as file:
        token = file.readline().strip()
    return token
API_TOKEN = read_api_token()

genai.configure(api_key=API_TOKEN)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")

print(response.text)