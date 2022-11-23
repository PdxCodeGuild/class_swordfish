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
# print(f'Quote: {quote} Author: {author}')

keyword = input('Enter a keyword to search for quotes: ')
response = requests.get(f'https://favqs.com/api/quotes?filter={keyword}',
                        headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
json_response = response.json()
quotes_list = json_response['quotes']
for quote in quotes_list:
    author = quote['author']
    quote = quote['body']
    print('\n')
    print(author)
    print(quote)

page = json_response['page']
print('page', page)
print('last_page', json_response['last_page'])


while True:
    user_input = input('Enter "next page", "new search", "done": ')
    if user_input == 'next page':
        print('User wants next page')
        if json_response['last_page'] == False:
            page += 1
        else:
            print('This is the end of your search')
            continue
    elif user_input == 'new search':
        print('User wants a new search')

    elif user_input == 'done':
        print('User wants to exit the program')
        break
    else:
        # -->The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
        continue

    # allow the user to find quotes by keyword
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}',
                            headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

    # print(type(response))  # --> class Response object
    json_response = response.json()
    # print(type(json_response))  # --> class dict
    # print(json_response.keys())  # -->dict_keys(['page', 'last_page', 'quotes'])
    quotes_list = json_response['quotes']
    # print(type(quotes_list))  # --> class list
    the_first_quote = quotes_list[0]
    # print(type(the_first_quote))  # --> class dict
    # print(the_first_quote.keys())
    # dict_keys(['id', 'dialogue', 'private', 'tags', 'url', 'favorites_count', 'upvotes_count', 'downvotes_count', 'author', 'author_permalink', 'body'])
    quote_body = the_first_quote['body']
    # print(quote_body)

   # print(type(quotes_list[1]))
    for quote in quotes_list:
        author = quote['author']
        quote = quote['body']
        print('\n')
        print(author)
        print(quote)

    print('page', json_response['page'])
    print('last_page', json_response['last_page'])
