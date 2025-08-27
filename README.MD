# Your Support & Feedback is important 💙💙💙 [TechWebDots on YouTube](https://www.youtube.com/@TechWebDots)
1. Please rate us on Google https://g.page/SoftwareCoding?gm that will also be like a cofee of motivation. ☕🙂
2. You can also write us at 📧 admin@techwebdots.in or quickly contact us at 📞+91-7303751089.
3. Visit 🌐 https://www.TechWebDots.in for any Consulting.
4. Information Discussed in the session & Short notes for quick reference given below-

# URLs
1. https://pypi.org/
2. https://fastapi.tiangolo.com/
3. https://fastapi.tiangolo.com/learn/

# Commands:
1. py -3.12 -m venv fapivenv
2. .\fapivenv\Scripts\activate
3. pip install "fastapi[standard]"
4. pip freeze > requirements.txt
5. pip install -r requirements.txt
6. fastapi dev main.py
7. pip cache purge 
8. deactivate
9. pip install pip_search
10. ip install --upgrade pip setuptools
```
Open your browser at http://127.0.0.1:8000/
You will see the JSON response as:
{"Hello": "Welcome to Python FastAPI World!"}

Open your browser at http://127.0.0.1:8000/items/5?q=somequery.
You will see the JSON response as:
{"item_id": 5, "q": "somequery"}

Interactive API docs
Now go to http://127.0.0.1:8000/docs.
You will see the automatic interactive API documentation (provided by Swagger UI).

Alternative API docs
And now, go to http://127.0.0.1:8000/redoc.
You will see the alternative automatic documentation (provided by ReDoc)
```
# To setup & run FastAPI on Azure function on local Machine (Perform as Admin)

7. Add meaningful /health route as best practice
8. Understand Running Server Manually - fastapi run main.py  
- When you install FastAPI, it comes with a production server, Uvicorn, and you can start it with the fastapi run command.
- FastAPI uses a standard for building Python web frameworks and servers called ASGI. FastAPI is an ASGI web framework.
- You need an ASGI server program like Uvicorn to run a FastAPI/ASGI app in a remote server machine, this is the one that comes by default in the fastapi command.
9. Understand Running server program - 
- uvicorn finename:app
- main refers to the main.py file. (the Python "module").
- app refers to the FastAPI instance created in main.py; app = FastAPI()
- uvicorn finename:app --host 0.0.0.0 --port 80 (It is equivalent to: from main import app)
- [uvicorn details](https://fastapi.tiangolo.com/deployment/manually/#server-machine-and-server-program)
10. [optional] AZURE CLI install & run az --version
- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=winget
11. Install Azure functions Core Tools 4.x and run func --version (upgrade if already installed)
- Download and run the Core Tools installer : https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python
12. Install Azure Tools from extensions in Visual Studio Code
13. Setup the Azure function Locally first & test. run func init .
14. Install the python version 3.12.* if required from python website and Select the right python version VS code editor.
15. If changing the python version because of any reason, please recreate the environment after deleting the old environment only, make sure to reload the VS code editor.
16. Update the function_app.py, main.py, requirements.txt and host.json 

# ZIP Deply Python FastAPI on Azure Functions 
17. Prepare AZ Functions (Single Function Structure) Required files and their significance for python FASTApi
```
python-fastapi/
│
├── main.py 			# Required with FASTApi code
├── function_app.py		# Required Azure Function or FastAPI ASGI entry point with FASTApi object reference
├── requirements.txt 	# Required with all the python packages
├── host.json 			# Required by Azure Function With routePrefix = ""
├── .funcignore     	# Optional for simple case but recommended
├── __init__.py 		# Optional for simple case classic model, can be empty file, not strictly needed but good practice
├── function.json 		# Optional for simple case Metadata for your function
```

18. Create python based Azure function from azure portal
19. Create the zip file with all the required content
20. Prepare Azure zip deployment commands with cleanup - https://learn.microsoft.com/en-us/azure/azure-functions/deployment-zip-push
``` python
az login --tenant xxx-xxx-xxx---xxxx
after login you will get the option to set subcription otherwise you can run the below command
az account set --subscription <subscription_id_or_name>
```
## App Settings Cleanup & FunctionApp Deployment Commands
``` python
- Delete a function apps settings command.
az functionapp config appsettings delete --resource-group {resource_group} --name {fun_app_name} --setting-names SCM_DO_BUILD_DURING_DEPLOYMENT
- Perform deployment using the kudu zip push deployment for a function app. Add in the AppSetting SCM_DO_BUILD_DURING_DEPLOYMENT = true
az functionapp deployment source config-zip --resource-group {resource_group} --name {fun_app_name} --src "{zip_file_path}" --build-remote true
```
## Important: When you use .zip deployment, any files from an existing deployment that aren't found in the .zip file are deleted from your function app.
21. Test the AZURE function from AZ portal
22. In case of multiple functions, Split each function into its own folder, Each folder has its own function content but there will be single zip.

# [Azure Function App Logging & KUDU URL Watch Now](https://youtu.be/VPWvxD7Kpeo?feature=shared)
```Get kudu URL
Function URL: https://fun-app-fast-api.azurewebsites.net/
KUDU URL: https://fun-app-fast-api.scm.azurewebsites.net/

KUDU References
- https://github.com/projectkudu/kudu/wiki/
- https://learn.microsoft.com/en-us/azure/app-service/resources-kudu

// KQL Example to run in Logs App
// Request count trend 
// Chart Request count over the last day. 
// To create an alert for this query, click '+ New alert rule'

requests
| where name == "fast-api-fun"
| summarize totalCount=sum(itemCount) by bin(timestamp, 30m)
| render timechart

requests 
| where name =="fast-api-fun"
```
23. Check deployment status, 
24. Where to check Logs, Log stream, App Insights, Check Logs (KQL example), Compare with AppService based 
25. pip install python-dotenv
26. Create .env file
27. Add Key-Value-pair = > API_KEY=my_secret_key
28. Code Changes
```
	import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Access the variables using os.getenv()
    api_key = os.getenv("API_KEY")
    print(f"API Key: {api_key}")
```
# Access Storage Account File From Azure Function App By using .env key variable locally & on Azure Production
1. Create A CONTAINER & Add a file
2. Get the storage account connection string key 
3. Set the storage account connection string key in .env file 
4. Add required Azure Package & Import Statements “azure-storage-blob”
5. Add Read-File-From-Container method/route and read the key from .env file
6. Test Code Changes locally
7. [PROD] Add the key in Function App Settings (if not already exist)
8. pip freeze > requirements.txt 
9. Zip Deploy the function on Azure 
10. Test Code Changes on Azure Portal

# Azure Functions | Key Vault Secret | Pyhton | FastAPI | Zip Deploy | HTTP Trigger
1. Zip Deploy Python FatsAPI Function in Azure Function App locally & in Azure Portal
2. #azure Function App http trigger access Key Vault
3. Create a Azure Key Vault from scratch & Add Secret #azurefunctions #httptrigger #fastapi 
4. For PRODUCTION Configure the Azure Function with identity enable and Set the Role "Key Vault Secrets User" on Key Vault for permission & set the user permission with "Key Vault Administrator" for local setup, also Added required Azure Package & Import Statements “azure-keyvault-secrets”
5. Add Read-File-From-Key-Vault-Secret method or route and read the secret and Test the Code Changes locally
6. Zip Deploy the function on Azure & Test Code Changes on Azure Portal
7. Generate updated pip freeze requirements.txt

# Azure Functions Read & Write on Cosmos DB NoSQL | Pyhton | FastAPI
1. Create a Azure Cosmos DB from scratch 
2. For PRODUCTION Configure the Azure Function with CosmosDB keys Primary Connection String & Test the Code Changes locally Using .env file
3. pip install azure-cosmos
4. Add from azure.cosmos import CosmosClient
6. GitHub Actions Workfloe to Deploy the function on Azure & Test Code Changes on Azure Portal
7. Generate updated requirements.txt

# Azure Functions Read & Write on Cosmos DB NoSQL | Pyhton | FastAPI
1. pip install redis
2. import redis 
3. pip freeze > requirements.txt