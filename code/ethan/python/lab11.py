# Quotes API

from email.quoprimime import quote
import requests
import pprint

answer = 'next page'

quote_type = input('Enter a keyword to search for quotes: ')

page = 1

while answer == 'next page':

    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={quote_type}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Content-Type': 'application/json'})

    results = response.json()

    print(f'25 quotes associated with {quote_type} - page {page}\n')

    x = 0

    for _ in results['quotes']:

        print_quote = results['quotes'][x]['body']

        author = results['quotes'][x]['author']

        print(f'"{print_quote}"')
        print(f'-{author}\n')

        x+=1

    answer = input("Enter 'next page' or 'done': ")

    if answer == 'next page':
    
        page += 1