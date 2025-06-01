import azure.functions as func
import datetime
import json
import logging
from main import app as fastapi_app

app = func.AsgiFunctionApp(app=fastapi_app, function_name="fast-api-fun", http_auth_level=func.AuthLevel.ANONYMOUS)
