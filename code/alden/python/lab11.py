# Quote API

import requests
import pprint

data = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
result = data.json()
# pprint.pprint(result)

print(f'"{result["quote"]["body"]}" -{result["quote"]["author"]}')