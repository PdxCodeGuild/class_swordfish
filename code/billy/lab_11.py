'''
program: lab_11
author: billy frick
date: 26 september 2022

function:   > this program will retrieve quotes off of https://favqs.com/api/qotd.
            > the program will prompt the user for a key word, and bring up relating quotes.

'''

# imports
import time
import requests
import json
import pprint

response = requests.get('https://favqs.com/api/qotd', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

quote_dict = json.loads(response.text)

print('\n',quote_dict['quote']['body'])
print('\n\t-',quote_dict['quote']['author'])


# def quote_keyword_result(keyword):

keyword = input("\n> To begin your search for quotes, please enter a keyword: ")

keyword_response = requests.get(f'https://favqs.com/api/quotes?page=<page>&filter={keyword}', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

keyword_quotes = json.loads(keyword_response.text)

print(keyword_quotes)

print(type(keyword_quotes))