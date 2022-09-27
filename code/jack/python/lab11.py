# Lab 11: Quotes API

import requests

parameters = {'page': 1}

def get_quotes(): # returns list of quote dictionaries
    response = requests.get('https://favqs.com/api/quotes', headers={'accept': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = parameters)
    results = response.json()
    quotes = results['quotes']

    if quotes[0]['body'] == 'No quotes found':
        print(quotes[0]['body'])
    else:
        print(f'{len(quotes)} quotes associated with {parameters["filter"]} - page {parameters["page"]}')
        for dict in quotes: # prints each quote/author from list of quote dictionaries
            quote = dict['body']
            author = dict['author']
            output = '-' + quote + ' -' + author
            print(output)
    

# collect keyword, first output
parameters['filter'] = input('Enter a keyword to search for quotes: ')
print('\n')
get_quotes()


# REPL for subsequent pages of quotes
while True:
    command = input('Enter \'next page\', \'done\', or \'new term\': ')

    if command == 'done':
        break
    elif command == 'next page':
        parameters['page'] += 1
        get_quotes()
    elif command == 'new term':
        parameters['page'] = 1
        parameters['filter'] = input('Enter a new keyword to search for quotes: ')
        get_quotes()
    else:
        print('Invalid input')
