'''
program: lab_11
author: billy frick
date: 7 october 2022

function:   > this program will retrieve quotes off of https://favqs.com/api/qotd.
            > the program will prompt the user for a key word, and bring up related quotes.
            > the user will enter a REPL to enter a new keyword, go to the next page of quotes given or exit the program.

'''

# imports
from wsgiref import headers
import requests
import json
import pprint

# grabs response from quotes API generator. 
response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

# saves the response to variable 'quote_dict' as text str.
quote_dict = json.loads(response.text)

# prints a random quote, and the author.
print('\n',quote_dict['quote']['body'])
print('\n\t-',quote_dict['quote']['author'])

def get_quotes(page, keyword):
    '''
    pulls page, user defined keyword and the 'last_page' boolean from API. Returns all variables.
    '''
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    json_data = json.loads(response.text)
    is_last_page = json_data.get('last_page')
    page_number = json_data.get('page')
    quotes = json_data.get('quotes')
    return quotes, is_last_page, page_number

def print_quotes(quotes):
    '''
    searches for the quotes and authors, and prints each one on a new line.
    '''
    for quote in quotes:
        quote_body = quote['body']
        quote_author = quote['author']
        print(quote_body,'\n\t-', quote_author, '\n')
    
page = 1
keyword = input("\n> To begin your search for quotes, please enter a keyword: ")
quotes, is_last_page, page = get_quotes(page, keyword)

print_quotes(quotes)
print('\nyou are currently on page',page,'.')

while True:
    user_response = input("\nwould you like to enter a new keyword, go to the next page (if applicable) or exit the program? [new, next, exit]: ")

     # if user wants a new search, they will be promted for a new keyword. get_quotes and print_quotes functions will be used.
    if user_response == 'new':
        page = 1 # resets page number to 1 for a new keyword.
        keyword = input('\nplease enter a word to search for related quotes: ')
        quotes_in_loop, is_last_page, page = get_quotes(page, keyword)
        print_quotes(quotes_in_loop)
        print('\nyou are currently on page', page, '.')

    # ends the program
    elif user_response == 'exit':
        print('\n\tthank you for using this program!\n')
        break

    # if there are more pages, a new request will be pulled and pages will gain +1. If there are no more pages, the user will be notified.
    elif user_response == 'next':
        if is_last_page == True:
            print("\n\t> there are no more pages <")
        else:
            page += 1
            quotes_in_loop, is_last_page, page = get_quotes(page, keyword)
            print_quotes(quotes_in_loop)
            print('\nyou are currently on page',page,'.')

    else:
        print('\n\t> please enter a valid command <')

