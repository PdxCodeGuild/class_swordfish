# Lab 10: Dad Joke API
import requests
import pprint

def get_joke(term = ''): 
    response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json', 'search_term': term})
    print(response)
    results = response.json()
    joke = results['joke']
    return joke

while True:
    print('(Type \'list\' for a list of commands)')
    command = input('Enter a command: ').lower()
    if command == 'exit':
        break
    elif command == 'list':
        print('\'exit\' to break\n\'joke\' to generate a joke\n\'term\' to add a term to the next joke')
    elif command == 'joke':
        print(get_joke())
    elif command == 'term': # does not work, unsure why
        term = input('Enter a term: ')
        print(get_joke(term))
    else:
        print('Invalid input')

