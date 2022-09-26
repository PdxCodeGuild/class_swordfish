# Lab 11: Quotes API

import requests

parameters = {'page': 1}

def get_quotes(): # returns list of quote dictionaries
    response = requests.get('https://favqs.com/api/quotes', headers={'accept': 'application/json','Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = parameters)
    results = response.json()
    return results['quotes']
  

def quotes_to_print(quotes): # takes list of quote dictionaries and prints quote + author for each dict
    print(f'{len(quotes)} quotes associated with {keyword} - page {parameters["page"]}')
    for dict in quotes:
        quote = dict['body']
        author = dict['author']
        output = '-' + quote + ' -' + author
        print(output)
        



keyword = input('Enter a keyword to search for quotes: ')
parameters['filter'] = keyword
print('\n')
quotes = get_quotes()
quotes_to_print(quotes)



# REPL
while True:
    command = input('Enter \'next page\' or \'done\': ')

    if command == 'done':
        break
    elif command == 'next page':
        parameters['page'] += 1
        quotes = get_quotes()
        quotes_to_print(quotes)
    else:
        print('Invalid input')