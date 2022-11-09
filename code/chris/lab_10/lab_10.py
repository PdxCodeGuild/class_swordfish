import requests

import pprint

#Version 1
jokes = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'}) #headers is value of key

# print(jokes.url)
# # print(jokes.text)
# print(jokes.status_code)
# print(jokes.encoding)
# print(jokes.headers)

dad_results = jokes.json() #decode to list / dict

# print(dad_results)

# pprint.pprint(dad_results)

print(f'Your random joke is: {dad_results["joke"]}')

#Version 2 Optional
