import requests
import pprint
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

random_quote = json.loads(response.text)['quote']['body']
author = json.loads(response.text)['quote']['author']
print(random_quote, author)

