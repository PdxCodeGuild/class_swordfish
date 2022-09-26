import requests
import json




response = requests.get("https://favqs.com/api/qotd")

print(response.url)
print(response.status_code)