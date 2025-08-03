import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, 🚀 Welcome to Python FastAPI World with OIDC based special CICD pipeline!"}

@app.get("/health", status_code=200, response_description="Health Check")
def read_health():
    return {"status": "OK", "message": "Service is running"}

@app.get("/GetSecretByName", response_description="Get Secret By Name")
def read_GetSecretByName():
    try:
        # Replace with your vault name
        key_vault_url = "https://demo00.vault.azure.net/"

        # Automatically uses Managed Identity (Azure) or Azure CLI/MSAL (local)
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        # Retrieve a secret
        secret_name = "test"
        retrieved_secret = client.get_secret(secret_name)

        return {f"Secret Value: {retrieved_secret.value}"}
    except AzureError as e:
            print(f"Failed to connect or list blob: {e}")