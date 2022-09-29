import requests
import json
import pprint
"""Version 1: Get a random quote, parse the JSON in the response into a python dictionary, and show the quote and the author. """
#response = requests.get('https://favqs.com/api/qotd', headers= {'Content-Type': 'application/json'})
# results = response.json()
# response = requests.get('https://favqs.com/api/qotd', params={'format': 'json'}) #gtg
# print(response.text) #gtg
# data = response.json() #gtg
# #data = json.loads(response.text) #must use import json for this to work
# print(data['quote']['body']) #gtg
# print(data['quote']['author']) #gtg

"""Version 2: Prompt the user for a keyword, list the quotes you get in response, and prompt the user to either show the next page or enter a new keyword."""
keyword = input("Enter a keyword: ")
print(f'25 words associated with {keyword}')
#kw_response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter=+{keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) #this is the way: adds user input to URL string
kw_response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter=+{keyword}', params={'format': 'json'}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
#quote_auth = kw_response.json()
kw_quotes = kw_response.json()
#print(kw_quotes.keys()) #dict_keys(['page', 'last_page', 'quotes']) --- can call a method on dicts; if last page = true)
quotes_list = kw_quotes['quotes']

All above is same!

for quote in quotes_list:
    author = quote['author']
    body = quote['body']
    print(body, author)
#pprint.pprint(quotes_list)
#pprint.pprint(kw_quotes) #green is class, yellow is method
(or while is false, do this)
    page = kw_quotes['page'] + 1
if kw_quotes['last_page'] = 1 == True
    quit
else: blah






