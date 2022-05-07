import requests

endpoint = "https://httpbin.org/anything"#/status/200"

get_response = requests.get(endpoint)
print(get_response.json())
