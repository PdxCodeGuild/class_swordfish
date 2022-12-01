from unittest import result
import requests
import json
import pprint
import time
import re
# response = requests.get('https://favqs.com/api/qotd/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
# results = response.json()

# authors = results['quote']['author']
# quotes = results ['quote']['body']
# # print(authors)
# print(quotes)

# while True:
#         response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
#         results = response.json()

#         authors = results['quote']['author']
#         quotes = results ['quote']['body']
#         user_input = input('Would you like a quote?: ')                   #this code block spits out a random quote with the author above it
  

#         if user_input == 'yes':
#             print(authors)
#             print(quotes)
#             pass
#         elif user_input == 'no':
#             print('Goodbye')
#             break
#         else:
#             print('Invalid option. Yes or No response required')
# https://favqs.com/api/quotes?page=<page>&filter=<keyword>

# page = input('What page would you like?: ')
while True:

    keyword= input('What keyword would you like to search for?: ')
    response = requests.get('https://favqs.com/api/quotes/?page='+keyword+'&type=tag', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = params)
    results = response.json()
    # pprint.pprint(results)
    combined_quotes = results ['quotes']
    quotes = combined_quotes [::]

# authors_and_quotes = []

    for i, value in enumerate(combined_quotes):
        print(combined_quotes[i]['author'])
        print(combined_quotes[i]['body'])

    second_user_input = input('Would you like to view the next page or a new keyword?: ')

    if second_user_input == 'new keyword':
        keyword= input('What keyword would you like to search for?: ')
        response = requests.get('https://favqs.com/api/quotes/?filter='+keyword+'&type=tag', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        results = response.json()
# print(results)
        combined_quotes = results ['quotes']
        quotes = combined_quotes [::]

        for i, value in enumerate(combined_quotes):
            print(combined_quotes[i]['author'])
            print(combined_quotes[i]['body'])
    # for val in combined_quotes[i]['body']:
        # print (val)
    elif second_user_input == 'next page':
        for i, value in enumerate(combined_quotes):
            print(combined_quotes[i]['author'])
            print(combined_quotes[i]['body'])

    elif second_user_input == 'no':
        print('Goodbye')

# authors = combined_quotes['authors']

# print(quotes)