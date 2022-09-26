# Lab 10: Dad Joke API
import requests
import pprint

parameters = {} # empty dictionary to populate with search parameters

def get_joke(): 
    response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'},  params = parameters)
    results = response.json()
    joke = results['results'][0]['joke']
    return joke

while True:
    print('(Type \'help\' for a list of commands)')
    command = input('Enter a command: ').lower()
    if command == 'e':
        break
    elif command == 'help':
        print('\'e\' to break\n\'j\' to generate a joke\n\'term\' to add a term to the next joke\n\'c\' to clear search parameters')
    elif command == 'j':
        print(get_joke())
    elif command == 't': # does not work, unsure why
        parameters['term'] = input('Enter a term: ')
    elif command == 'c':
        parameters = {}
        print('Parameters cleared')
    else:
        print('Invalid input')

