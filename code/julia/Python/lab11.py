# Quotes API
import requests
import pprint
import json
import time

###-----Version 1: Get a Random Quote-----###
# quotes_api = requests.get('https://favqs.com/api/qotd', headers = {'Content-Type': 'application/json'})#
# #results = quotes_api.json()
# r#esponse = requests.get('https://favqs.com/api/qotd', params={'format': 'json'})
# p#rint(response.text)

#data = quotes_api.json()#
#data = json.loads(quotes_api.text)#

# print(f"The Quote: {data['quote']['body']}")#
# print(f"The Author: {data['quote']['author']}")#


###-----Version 2: List Quotes by Keyword-----###

keyword = input("Enter a keyword to search for quotes: ")
print(f'Loading page with a list of quotes associated with the word {keyword}...: ')

response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter={keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

keyword_quotes = response.json()
# print(response.text)
page = 1

list_of_quotes = keyword_quotes['quotes']
time.sleep(3)
for quote in list_of_quotes:
    author = quote['author']
    body = quote['body']
    print(body)
    print(author,"\n")

while True:

    user_selected = input("Enter 'next page' for more quotes, 'new search' to enter a new search keyword or 'exit' to exit:\n >>> ")
    if user_selected == 'next page':
        page = keyword_quotes['page'] + 1
        response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter={keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        keyword_quotes = response.json()
        for x in keyword_quotes['quotes']:
             author = quote['author']
             body = quote['body']
             print(x['body'])
             print(x['author'],"\n")

    elif user_selected == 'new search':
        keyword = input("Enter a new keyword:\n")
        response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter={keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
        keyword_quotes = response.json()
        for word in keyword_quotes['quotes']:
            auth = quote['author']
            bod = quote['body']
            print(auth,"\n", bod, "\n")




        

     
        
        

