import requests

endpoint = "http://localhost:8000/dates/19"

get_response = requests.delete(endpoint)
# get_response.raise_for_status()
if get_response.status_code == 500:
    print('Error! Status code: ')
if get_response.status_code != 204:
    print(get_response.status_code)
