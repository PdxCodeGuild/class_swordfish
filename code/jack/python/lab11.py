# Lab 11: Quotes API

import requests

def get_quote():
    response = requests.get('https://favqs.com/api/qotd', headers={'accept': 'application/json'})
    results = response.json()
    quote = results['quote']['body']
    author = results['quote']['author']
    print(f'{quote} -{author}')

get_quote()