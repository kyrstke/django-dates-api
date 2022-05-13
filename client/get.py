import requests

endpoint = "http://localhost:8000/dates/"

get_response = requests.get(endpoint)
get_response.raise_for_status()
if get_response.status_code != 204:
    print(get_response.json())
