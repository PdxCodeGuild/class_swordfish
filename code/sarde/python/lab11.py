from ast import While
import requests
import pprint
'''Lab 11: Quotes API
'''
'''
-Using the Favqs Quotes API to first get a random quote
-And then allow the user to find quotes by keyword
-To accomplish this we'll be using the requests library.
'''
'''Version 1: Get a Random Quote
    -The URL to get a random quote is https://favqs.com/api/qotd,
    -Send a request here,
    -Parse the JSON in the response into a python dictionary,
    -and show the quote and the author.
'''
'''
response = requests.get('https://favqs.com/api/qotd')
# print(response)  # --> <Response [200]>
# print(response.text)  # -->class str --> raw response
# parse JSON object into a dictionary
json_dict = response.json()
# print(json_dict)  # --> class dict
# print(json_dict.keys())
# dict_keys(['qotd_date', 'quote'])
quote = json_dict['quote']['body']
# print(quote)
author = json_dict['quote']['author']
# print(f'Author: {author}  Quote: {quote}')
'''
'''Version 2: List Quotes by Keyword
    -Prompt the user for a keyword,
    -List the quotes you get in response
    -Prompt the user to either show the next page
    -Or enter a new keyword
'''


def get_quotes(page, keyword):
    response = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}',
                            headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    # print(response.text)
    quotes_dict = response.json()
    # print(type(quotes_dict))  # --> class dict
    quotes_list = quotes_dict['quotes']
    # print(type(quotes_list))  # --> class list

    for quote in quotes_list:
        author = quote['author']
        quote = quote['body']
        print(f'Author: {author}\nQuote: {quote}\n')


keyword = input('Enter a keyword to search for quotes: ')
response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter={keyword}',
                        headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
# print(response.text)  # --> class str
quotes_dict = response.json()
# print(quotes_dict)  # --> class dict
# print(quotes_dict.keys())
# dict_keys(['page', 'last_page', 'quotes'])
quotes_list = quotes_dict['quotes']
# print(quotes_list)  # --> class list

# iterate over the quote_list
for quote in quotes_list:
    author = quote['author']
    quote = quote['body']
    print(f"Author: {author}\nQuote: {quote}")

page = quotes_dict['page']
last_page = quotes_dict['last_page']
print(f'page: {page}')  # --> page: 1
print(f'last page: {last_page}')  # --> last page: True


# REPL loop
while True:
    user_input = input('Enter "next page", "new search", "done": ')
    if user_input == 'next page':
        print('User wants to go to the next page')
        # page
        # keyword --> user wants the same search, and to go to the next page
        if quotes_dict['last_page'] == False:
            page += 1
        else:
            print('No more pages')
        # send a request to the API for the next page, after the loop

    elif user_input == 'new search':
        print('User wants a new search')
        keyword = input('Enter a new search word: ')
        print(keyword)

    elif user_input == 'done':
        print('User wants to exit the program')
        break

    else:
        print('Invalid user input, Try again')
        continue

    print('next page', page)

    get_quotes(page, keyword)
