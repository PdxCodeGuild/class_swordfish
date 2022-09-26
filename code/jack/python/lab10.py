# Lab 10: Dad Joke API
# issues: request should not be in get_joke fn- response states could be copied and manipulated for parameters, and efficiency
import requests


joke_i = 0 # joke index to track which joke the user last saw

p = { # dictionary to populate with search parameters
    'page': 1
}


def get_joke(joke_i): 
    response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'},  params = p)
    results = response.json()

    if results['total_jokes'] == 0:
        print('No jokes found')
    else:
        joke = results['results'][joke_i]['joke']
        print(joke)

        if joke_i + 1 == results['limit']: # if last joke on page, resets to first
            print(f'Last joke on page {results["current_page"]}')
            joke_i = 0
        else:
            joke_i += 1
    return joke_i

while True:
    command = input('Enter a command (Type \'help\' for a list of commands): ').lower()
    if command in ['exit', 'e']:
        break
    elif command == 'help':
        print('\'exit\' to exit the program\n\'joke\' to generate a joke\n\'term\' to add a term to the next joke\n\'clear\' to clear search p')
    elif command in ['joke', 'j']:
        joke_i = get_joke(joke_i)
    elif command == 'term':
        p['term'] = input('Enter a term: ')
    elif command == 'clear':
        p = {}
        print('Parameters cleared')
    elif command == 'next':
        joke_i = 0
        p['page'] += 1
    elif command == 'previous':
        if p['page'] == 1:
            print('You are already on the first page.')
        else:
            p['page'] -= 1
            joke_i = 0
    else:
        print('Invalid input')

