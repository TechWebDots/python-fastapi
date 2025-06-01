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
1. python -m venv fapivenv
2. .\fapivenv\Scripts\activate
3. pip install "fastapi[standard]"
4. pip freeze > requirements.txt
5. pip install -r requirements.txt
6. fastapi dev main.py
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
15. Update the function_app.py, main.py, requirements.txt and host.json 