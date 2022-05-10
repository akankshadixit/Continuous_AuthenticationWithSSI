import requests

requests.get("http://steward:5000/start_steward_agent")
requests.get("http://supplier:5000/start_supplier_agent")