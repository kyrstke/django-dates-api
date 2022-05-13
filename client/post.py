import requests

local_endpoint = "http://localhost:8000/dates/"
heroku_endpoint = 'https://django-dates-api.herokuapp.com/dates/'

data = {
    "month": 9,
    "day": 19
}

get_response = requests.post(heroku_endpoint, json=data)
get_response.raise_for_status()
if get_response.status_code != 204:
    print(get_response.json())
