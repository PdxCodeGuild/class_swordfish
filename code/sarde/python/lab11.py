'''Lab 11: Quotes API
'''
'''
-using the Favqs Quotes API to first get a random quote,
-and then allow the user to find quotes by keyword
'''
import requests
import pprint
response = requests.get(
    'https://favqs.com/api/qotd', headers={'accept': 'application/json'})
# print(response.text)
quote = response.json()['quote']['body']
# print(quote)
