import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, 🚀 Welcome to Python FastAPI World with OIDC based special CICD pipeline!"}

@app.get("/health", status_code=200, response_description="Health Check")
def read_health():
    return {"status": "OK", "message": "Python FastAPI Azure Function is running"}

@app.get("/GetSecretByName", response_description="Get Secret By Name")
def read_GetSecretByName():
    try:
        # Replace with your vault name
        # Access the variables using os.getenv()
        key_vault_url = os.getenv("AZURE_KEYVAULT_URL")
        # key_vault_url = "https://demo00.vault.azure.net/"

        # Automatically uses Managed Identity (Azure) or Azure CLI/MSAL (local)
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=key_vault_url, credential=credential)

        # Retrieve a secret
        secret_name = "test"
        retrieved_secret = client.get_secret(secret_name)

        return {f"Secret Value: {retrieved_secret.value}"}
    except AzureError as e:
            print(f"Failed to connect or list blob: {e}")

@app.get("/GetJSONDoc", response_description="Get Cosmos JSON Doc")
def read_GetJSONDoc():
    try:        
        # Access the variables using os.getenv()
        cosmosdb_url = os.getenv("AZURE_COSMOSDB_URL")

        # Automatically uses Managed Identity (Azure) or Azure CLI/MSAL (local)
        credential = DefaultAzureCredential()
        # client = CosmosClient(url=cosmosdb_url, credential=credential)
        client = CosmosClient.from_connection_string(cosmosdb_url)
        database = client.get_database_client("cosmicworks")
        print(f"Get database:\t{database.id}")
        container = database.get_container_client("products")
        print(f"Get container:\t{container.id}")
        new_item = {
            "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            "category": "gear-surf-surfboards",
            "name": "Yamba Surfboard",
            "quantity": 12,
            "sale": False,
        }

        created_item = container.upsert_item(new_item)
        print(f"Upserted item:\t{created_item}")
        existing_item = container.read_item(
            item="aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
            partition_key="gear-surf-surfboards",
        )

        return {f"New Item Inserted Successfully: {existing_item}"}
    except AzureError as e:
            print(f"Failed to connect Cosmos DB : {e}")