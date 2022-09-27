import requests
import pprint

#Version 1
# quote = requests.get('https://favqs.com/api/qotd', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}) #headers is value of key

# # print(quote.url)
# # print(quote.text)
# # print(quote.status_code)
# # print(quote.encoding)
# # print(quote.headers)

# random_q = quote.json() #decode
# # pprint.pprint(random_q) #print python dictionary
# # body = pprint.pprint(random_q['quote']['body'])
# # print(body)
# # author = pprint.pprint(random_q['quote']['author'])
# # the_keys = random_q.keys() 
# # print('printing the keys:', the_keys) #<<<-------------------------------********************* GET KEYS TO DICT.


# the_author = random_q['quote']['author']
# the_body = random_q['quote']['body']
# # print('the author: ', the_author)
# # print('the body: ', the_body)

# print(f"""VERSION 1 ANSWER:
# Your random quote is: {the_body} 
# - {the_author}""") # parse dictionary to show the quote and the author

# #Version 2

# # I NEED TO LIST QUOTES BY KEYWORD... url parameters an API takes and the response and use filter parameter
# # prompt user for a keyword
# # list quotes i get keyword
# # prompt user to show next page of quotes
# # enter a new keyword
request = input('What would you like to do? ')
user_prompt = input('Please enter a keyword to search for quotes: ')
# print(user_prompt)
response = requests.get('https://favqs.com/api/quotes', params={'filter': user_prompt, 'page': 0}, headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b'})

# print('This is the quote:', quote)
# print(quote.url)
# print(quote.text)
# print(quote.status_code)
# print(quote.encoding)
# print(quote.headers)

results = response.json() 
quotes = results['quotes']


print(request)
while True:
    if request == 'search keyword':
        for quote in quotes:
            print(quote['body'])
            print(quote['author'] + '\n')
    elif request == 'next page':
        for quote in quotes:
            print(quote['body'])
            print(quote['author'] + '\n')
    elif request == 'done':
        break
    else:
        print('Try Again!')