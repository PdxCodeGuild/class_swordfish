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

page = 1

while True:
        
    print(f'Loading page with a list of quotes associated with the word {keyword}... \n')


    response = requests.get(f'https://favqs.com/api/quotes?', params={'filter': keyword, 'page': page}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    keyword_quotes = response.json()
    

    list_of_quotes = keyword_quotes['quotes']
    time.sleep(3)
    for quote in list_of_quotes:
        author = quote['author']
        body = quote['body']
        print(body)
        print(author,"\n")

    next_move = input("Type 'next' for next page, 'new' for new search or 'done' to exit: ")
    if next_move == 'next':
        page += 1

    elif next_move == 'new':
        keyword = input("Enter a new word: ")
        page = 1

    else:
        break
   






        

     
        
        

