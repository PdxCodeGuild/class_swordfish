'''Lab 11: Quotes API
'''
'''
-using the Favqs Quotes API to first get a random quote,
-and then allow the user to find quotes by keyword
'''
# get random quote
import requests
import pprint
response = requests.get(
    'https://favqs.com/api/qotd', headers={'accept': 'application/json'})  # -->get random quote
# print(response.text)
quote = response.json()['quote']['body']
author = response.json()['quote']['author']
#print(f'Quote: {quote} Author: {author}')


#input_page = input('Enter "next page" or "done": ')
page = 1
#input_keyword = input('Enter a keyword to search for quotes: ')
input_keyword = 'cats'
# allow the user to find quotes by keyword
response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={input_keyword}',
                        headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

print(type(response))  # --> class Response object
json_response = response.json()
print(type(json_response))  # --> class dict
print(json_response.keys())  # -->dict_keys(['page', 'last_page', 'quotes'])
quotes_list = json_response['quotes']
print(type(quotes_list))  # --> class list
the_first_quote = quotes_list[0]
# for i in range(len(quotes_list)):
print(type(the_first_quote))  # --> class dict
print(the_first_quote.keys())
#dict_keys(['id', 'dialogue', 'private', 'tags', 'url', 'favorites_count', 'upvotes_count', 'downvotes_count', 'author', 'author_permalink', 'body'])
quote_body = the_first_quote['body']
print(quote_body)

same_quote_body = response.json()['quotes'][0]['body']
print(same_quote_body)

# for i in range(len(same_quote_body))
