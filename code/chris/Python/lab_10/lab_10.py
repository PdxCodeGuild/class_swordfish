import requests

import pprint

#Version 1
jokes = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'}) #headers is value of key
dad_results = jokes.json() #decode to list / dict
print(f'Your random joke is: {dad_results["joke"]}')


#Version 2 Optional
jokes = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'})

# print(jokes.url)
# # print(jokes.text)
# print(jokes.status_code)
# print(jokes.encoding)
# print(jokes.headers)

dad_results = jokes.json()

pprint.pprint(dad_results)

while True:
    joke_type = input('Please enter a joke type you are searching for: ')
