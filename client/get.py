import requests

local_endpoint = "http://localhost:8000/dates/"
# heroku_endpoint = 'https://django-dates-api.herokuapp.com/dates/'

get_response = requests.get(local_endpoint)
get_response.raise_for_status()
if get_response.status_code != 204:
    print(get_response.json())
