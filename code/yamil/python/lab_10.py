import requests
import json
import time

response = requests.get('https://icanhazdadjoke.com/', headers ={'accept' : 'Application/json'})

# print(response.url)
# print(response.status_code)
# print(response.encoding)
# print(response.headers)

joke_dict = response.json()
# print(joke_dict)
dad_joke = joke_dict["joke"]
print(dad_joke)
