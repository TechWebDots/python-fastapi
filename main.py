import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

from azure.core.exceptions import AzureError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.cosmos import CosmosClient
import redis

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

@app.get("/CheckRedisOperations", response_description="Check Redis Operations")
def read_CheckRedisOperations():    
    try:
        # Connection details for your cache
        # Get the connection details for the Redis instance
        REDIS_HOST = os.getenv("AZURE_REDIS_URL")
        REDIS_PORT = int(os.getenv("AZURE_REDIS_PORT")) #For an Azure
        REDIS_PASSWORD = os.getenv("AZURE_REDIS_PWD")
        print("🚀 Starting Azure Redis Cache connection test...")
        print(f"📡 Connecting to: {REDIS_HOST}:{REDIS_PORT}")

        # Create credential provider using DefaultAzureCredential for Azure Entra ID authentication
        # credential_provider = create_from_default_azure_credential(("https://redis.azure.com/.default",),)
        
        # Create a Redis client with Azure Entra ID authentication
        r = redis.Redis(
            host=REDIS_HOST, 
            port=REDIS_PORT, 
            password=REDIS_PASSWORD,
            ssl=True, # Use SSL for port 6380
            decode_responses=True, # Decode responses to Python strings
            socket_timeout=10,
            socket_connect_timeout=10
            )
        # Ping the Redis server to test the connection
        result = r.ping()
        if result:
            print("✅ Ping returned: ", result)
        print()  # Add a new line

        # Create a simple set and get operation
        result = r.set("Message", "Hello, The cache is working with Python!")
        print("✅ SET Message succeeded: " + str(result))
        print()  # Add a new line

        value = r.get("Message")

        if value is not None:
            print("✅ GET Message returned : " + str(value))
            print()  # Add a new line
        else:
            print("⚠️  GET Message returned None")
            print()  # Add a new line
        
        valueDeleted = r.delete("Message");

        if valueDeleted is not None:
            print("✅ Message deleted : " + str(valueDeleted))
            print()  # Add a new line
        else:
            print("⚠️  Message not deleted!")
            print()  # Add a new line

        print("🎉 All Redis operations READ, WRITE, DELETE completed successfully!")
        return {f"🎉 All Redis operations WRITE, READ, DELETE completed successfully for 'Message' Key: {value}"}
        print()  # Add a new line
    except redis.ConnectionError as e:
        print(f"❌ Connection error: {e}")
        print("💡 Check if Redis host and port are correct, and ensure network connectivity")
        print()  # Add a new line
    except redis.AuthenticationError as e:
        print(f"❌ Authentication error: {e}")
        print("💡 Check if Azure Entra ID authentication is properly configured")
        print()  # Add a new line
    except redis.TimeoutError as e:
        print(f"❌ Timeout error: {e}")
        print("💡 Check network latency and Redis server performance")
        print()  # Add a new line
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        if "999" in str(e):
            print("💡 Error 999 typically indicates a network connectivity issue or firewall restriction")
            print("   - Verify the Redis hostname is correct")
            print("   - Verify that you have logged in with Az CLI")
            print("   - Ensure the Redis cache is running and accessible")
        print()  # Add a new line
    finally:
    # Clean up connection if it exists
        if 'r' in locals():
            try:
                r.close()
                print("🔐 Redis connection closed")
            except Exception as e:
                print(f"❌ Error closing connection: {e}")