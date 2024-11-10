import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

class GoogleGenAIChain:
    def __init__(self, system_prompt: str, model: str = "gemini-1.5-flash", temperature: float = 0.0, max_tokens: int = None, timeout: int = None, max_retries: int = 2):
        self.system_prompt = system_prompt
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        self.max_retries = max_retries
        self.api_token = self.read_api_token()
        os.environ["GOOGLE_API_KEY"] = self.api_token
        
    @staticmethod
    def read_api_token():
        with open('../../geminai.txt', 'r') as file:
            return file.readline().strip()
    
    def create_prompt(self):
        return ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}")
        ])
    
    def create_llm(self)->ChatGoogleGenerativeAI:
        return ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            timeout=self.timeout,
            max_retries=self.max_retries,
        )
    
    def create_chain(self):
        prompt = self.create_prompt()
        llm = self.create_llm()
        return prompt | llm