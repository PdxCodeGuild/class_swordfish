import requests
import pprint
import json

response = requests.get('https://favqs.com/api/qotd', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})

random_quote = json.loads(response.text)['quote']['body']
author = json.loads(response.text)['quote']['author']
#print(random_quote, "--", author)

#Version 2 -- 25 results per page -- how do I go to the next 25 pages??
while True:
    keyword = input("Please enter keyword to search for quotes: ")
    
    res = requests.get('https://favqs.com/api/quotes/?filter=<keyword>', headers = {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'filter': keyword, 'page': 1})
    quotes = json.loads(res.text)['quotes']
    for dic in quotes:
        for key in dic:
            if key == "body":
                print(dic[key],'\n')
    next = input("Type 'next': next 25 quotes. 'new': new keyword search, or type 'exit' to exit: ")
    if next == "exit":
        break
    if next == "new":
        

    
#first_quote = quotes[0]
#print(first_quote)
#the_author = first_quote['author']
#the_same_author = json.loads(res.text)['quotes'][0]['author']
#print(the_same_author)
#print(the_author)
#print(type(quotes))

#pprint.pprint(quotes)