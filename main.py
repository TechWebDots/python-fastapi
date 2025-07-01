from typing import Union
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Welcome to Python FastAPI World!"}

@app.get("/health", status_code=200, response_description="Health Check")
def read_health():
    return {"status": "OK", "message": "Service is running"}

@app.get("/first", status_code=200, response_description="Health Check")
def read_health():
    return {"status": "OK", "message": "Service1 is running"}

# Access the variables using os.getenv()
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")

@app.get("/second", status_code=200, response_description="Health Check")
def read_health():
    return {"status": "OK", "message": f"Service2 is running  {api_key}"}