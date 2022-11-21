# Dad joke API

import requests
import pprint
import time

joke_type = input('What type of jokes would you like to hear?  One word answers only.: ')

response = requests.get(f'https://icanhazdadjoke.com/search?term={joke_type}', headers={'accept': 'application/json'})

# print(response.url)
# print(response.status_code)
# print(response.encoding)
# print(response.headers)

results = response.json()
results = results['results']

# pprint.pprint(results)

x=0
answer = 'yes'
for jokes in results:
    joke = results[x]['joke']
    joke = str(joke)
    while answer == 'yes':
        if '?' in joke:
            new_joke = joke.split('?')
            joke = new_joke[0]
            punchline = new_joke[-1]
            print(f'{joke}?')

            time.sleep(4)

            print(punchline)
            answer = input('Would you like to hear another joke?: ')
        elif ':' in joke:
            new_joke = joke.split(':')
            joke = new_joke[0]
            punchline = new_joke[-1]
            print(f'{joke}:')

            time.sleep(4)

            print(punchline)
            answer = input('Would you like to hear another joke?: ')
        elif '.' in joke:
            new_joke = joke.split('.')
            joke = new_joke[0]
            punchline = new_joke[-1]
            print(f'{joke}.')

            time.sleep(4)

            print(punchline)
            answer = input('Would you like to hear another joke?: ')
        elif '...' in joke:
            new_joke = joke.split('...')
            joke = new_joke[0]
            punchline = new_joke[-1]
            print(f'{joke}...')

            time.sleep(4)

            print(punchline)
            answer = input('Would you like to hear another joke?: ')
        else:
            print(joke)
            answer = input('Would you like to hear another joke?: ')
    x+=1
